from io import BytesIO

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Count, Q
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import get_template
from django.views import generic
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from xhtml2pdf import pisa

from .filters import PublisherFilter, BookFilter, AuthorFilter
from .forms import BookForm, CommentForm
from .models import Book, Bookshelf, Author, BookCollection, Publisher, Comment, BookSeries, ReadingPlan, MyTag, Brand
from .serializers import AuthorSerializer, BookSerializer, PublisherSerializer, BookshelfSerializer, \
    BookCollectionSerializer, BookSeriesSerializer, ReadingPlanSerializer, BrandSerializer


# from taggit.models import Tag


class FormListView(generic.edit.FormMixin, generic.ListView):
    def get(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        self.form = self.get_form(form_class)

        self.object_list = self.get_queryset()
        allow_empty = self.get_allow_empty()
        if not allow_empty and len(self.object_list) == 0:
            raise Http404('Empty list.')

        context = self.get_context_data(object_list=self.object_list, form=self.form)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        pass


class FormBooksView(FormListView):
    template_name = 'bookshelf/books.html'
    context_object_name = 'book_list'
    form_class = BookForm

    def get_queryset(self):
        """
        Return the book list in this bookshelf.
        """
        return Book.objects.order_by('original_name')

    def form_valid(self, form):
        form.update_registered_status(form)
        return super().form_valid(form)


class BookUpdateView(generic.UpdateView):
    model = Book
    fields = ['registered']
    template_name_suffix = '_update_form'


class BooksView(generic.ListView):
    """Class based view for book list"""
    template_name = 'bookshelf/books.html'
    queryset = Book.objects.all()
    context_object_name = 'book_list'
    # paginate_by = 10
    paginate_by = 10
    paginate_orphans = 5
    tag_slug_kwargs = 'tag_slug'

    def get_queryset(self):
        """
        Return the book list in this bookshelf with conditions.
        """
        tag = None
        tag_slug = self.kwargs.get(self.tag_slug_kwargs, None)
        if tag_slug:
            tag = get_object_or_404(MyTag, slug=tag_slug)
            book_list = self.queryset.filter(tags__in=[tag]).order_by('id')
        else:
            book_list = self.queryset.order_by('id')
        return book_list


class SearchBooksView(generic.ListView):
    """Search the books with the given keywords from original_name, chinese_name and isbn fields."""
    template_name = 'bookshelf/books.html'
    queryset = Book.objects.all()

    def get_queryset(self):
        val = self.kwargs.get('keywords')
        print(self.kwargs)
        if val:
            book_list = self.queryset.filter(
                Q(original_name__icontains=val) | Q(chinese_name__icontains=val) | Q(isbn__icontains=val)).distinct()
        else:
            book_list = Book.objects.none()
        return book_list


class BookSearch(generic.TemplateView):
    template_name = 'bookshelf/search_form.html'


class BookSearchResult(generic.ListView):
    model = Book
    queryset = Book.objects.all()
    template_name = 'bookshelf/books.html'

    def get_queryset(self, *args, **kwargs):
        val = self.request.GET.get('q')
        if val:
            book_list = self.queryset.filter(
                Q(original_name__icontains=val) | Q(chinese_name__icontains=val) | Q(isbn__icontains=val)).distinct()
        else:
            book_list = Book.objects.none()
        return book_list


def book_list(request, tag_slug=None):
    """Method based view for book list"""
    object_list = Book.objects.all().order_by('original_name')
    tag = None
    if tag_slug:
        tag = get_object_or_404(MyTag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag]).order_by('original_name')

    paginator = Paginator(object_list, 10)
    page = request.GET.get('page')
    try:
        book_list = paginator.page(page)
    except PageNotAnInteger:
        book_list = paginator.page(1)
    except EmptyPage:
        book_list = paginator.page(paginator.num_pages)
    return render(request, 'bookshelf/books.html', {'page': page, 'book_list': book_list, 'tag': tag})


class BookView(generic.DetailView):
    model = Book
    template_name = 'bookshelf/book.html'
    context_object_name = 'book'
    pk_book_kwarg = 'pk'

    def get_object(self, queryset=None):
        book_id = int(self.kwargs.get(self.pk_book_kwarg, None))
        try:
            book_info = Book.objects.get(id=book_id)
            tag_ids = book_info.tags.values_list('id', flat=True)
            similar_books = Book.objects.filter(tags__in=tag_ids).exclude(id=book_id)
            similar_books = similar_books.annotate(same_tags=Count('tags')).order_by('-same_tags', 'original_name')[:10]
            book_info.similar_books = similar_books
        except IndexError:
            raise Http404
        return book_info

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        comments = Comment.objects.filter(book=self.get_object()).order_by('created')
        data['comments'] = comments
        data['comment_form'] = CommentForm()
        return data

    def post(self, request, *args, **kwargs):
        new_comment = Comment(body=request.POST.get('body'), name=request.POST.get('name'), book=self.get_object())
        new_comment.save()
        return self.get(self, request, *args, **kwargs)


class AuthorsView(generic.ListView):
    template_name = 'bookshelf/authors.html'
    context_object_name = 'author_list'
    paginate_by = 20
    paginate_orphans = 5

    def get_queryset(self):
        """
        Return the author list.
        """
        return Author.objects.order_by('id')


class AuthorView(generic.DetailView):
    model = Author
    template_name = 'bookshelf/author.html'
    context_object_name = 'author'
    pk_author_kwargs = 'pk'

    def get_object(self, queryset=None):
        author_id = int(self.kwargs.get(self.pk_author_kwargs, None))
        try:
            author_info = Author.objects.get(id=author_id)
        except IndexError:
            raise Http404
        return author_info


class PublishersView(generic.ListView):
    template_name = 'bookshelf/publishers.html'
    context_object_name = 'publisher_list'
    paginate_by = 20
    paginate_orphans = 5

    def get_queryset(self):
        """
        Return the publisher list.
        """
        return Publisher.objects.order_by('name')


class PublisherView(generic.DetailView):
    model = Publisher
    template_name = 'bookshelf/publisher.html'
    context_object_name = 'publisher'
    pk_publisher_kwargs = 'pk'

    def get_object(self, queryset=None):
        publisher_id = int(self.kwargs.get(self.pk_publisher_kwargs, None))
        try:
            publisher_info = Publisher.objects.get(id=publisher_id)
        except IndexError:
            raise Http404
        return publisher_info


class BrandsView(generic.ListView):
    template_name = 'bookshelf/brands.html'
    context_object_name = 'brand_list'
    paginate_by = 20
    paginate_orphans = 5

    def get_queryset(self):
        """
        Return the brand list.
        """
        return Brand.objects.order_by('name')


class BrandView(generic.DetailView):
    model = Brand
    template_name = 'bookshelf/brand.html'
    context_object_name = 'brand'
    pk_brand_kwargs = 'pk'

    def get_object(self, queryset=None):
        brand_id = int(self.kwargs.get(self.pk_brand_kwargs, None))
        try:
            brand_info = Publisher.objects.get(id=brand_id)
        except IndexError:
            raise Http404
        return brand_info


class BookCollectionsView(generic.ListView):
    template_name = 'bookshelf/collections.html'
    context_object_name = 'collection_list'
    paginate_by = 20
    paginate_orphans = 5

    def get_queryset(self):
        """
        Return the author list.
        """
        return BookCollection.objects.order_by('id')


class BookCollectionView(generic.DetailView):
    model = BookCollection
    template_name = 'bookshelf/collection.html'
    context_object_name = 'collection'
    pk_collection_kwargs = 'pk'

    def get_object(self, queryset=None):
        collection_id = int(self.kwargs.get(self.pk_collection_kwargs, None))
        try:
            collection_info = BookCollection.objects.get(id=collection_id)
        except IndexError:
            raise Http404
        return collection_info


class DefaultMixin(object):
    """
    Default settings for view authentication, permissions, filtering and pagination.
    """
    # authentication_classes = (
    #     authentication.BasicAuthentication,
    #     authentication.TokenAuthentication,
    # )
    # permission_classes = (
    #     permissions.IsAuthenticated,
    # )
    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100
    filter_backends = (
        DjangoFilterBackend,
        # filters.BaseFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )


class AuthorViewSet(DefaultMixin, viewsets.ModelViewSet):
    """
    API endpoint for listing and creating authors.
    """
    queryset = Author.objects.order_by('nation')
    filter_class = AuthorFilter
    filter_backends = (filters.SearchFilter,)
    search_fileds = ('name', 'nation',)
    ordering_fields = ('name', 'nation',)
    serializer_class = AuthorSerializer

    def get_queryset(self):
        name = self.request.query_params.get('name')
        if name:
            queryset = Author.objects.filter(name=name)
        else:
            queryset = Author.objects.all()
        return queryset


class BookViewSet(DefaultMixin, viewsets.ModelViewSet):
    """
    API endpoint for listing and creating books.
    """
    queryset = Book.objects.order_by('original_name')
    filter_class = BookFilter
    filter_backends = (filters.SearchFilter,)
    search_fileds = ('isbn', 'original_name', 'chinese_name',)
    ordering_fields = ('isbn', 'original_name',)
    serializer_class = BookSerializer

    def get_queryset(self):
        isbn = self.request.query_params.get('isbn')
        if isbn:
            queryset = Book.objects.filter(isbn=isbn)
        else:
            queryset = Book.objects.all()
        return queryset


class PublisherViewSet(DefaultMixin, viewsets.ModelViewSet):
    """
    API endpoint for listing and creating publishers.
    """
    queryset = Publisher.objects.all()
    search_fileds = ('name',)
    filter_backends = (filters.SearchFilter,)
    filter_class = PublisherFilter
    serializer_class = PublisherSerializer
    ordering_fields = ('name',)

    def get_queryset(self):
        name = self.request.query_params.get('name')
        if name:
            queryset = Publisher.objects.filter(name=name)
        else:
            queryset = Publisher.objects.all()
        return queryset


class BookshelvesView(generic.ListView):
    template_name = 'bookshelf/bookshelves.html'
    context_object_name = 'bookshelf_list'
    paginate_by = 20
    paginate_orphans = 5

    def get_queryset(self):
        """
        Return the bookshelf list.
        """
        return Bookshelf.objects.order_by('name')


class BookshelfView(generic.DetailView):
    model = Bookshelf
    template_name = 'bookshelf/bookshelf.html'
    context_object_name = 'bookshelf'
    pk_bookshelf_kwargs = 'pk'

    def get_object(self, queryset=None):
        bookshelf_id = int(self.kwargs.get(self.pk_bookshelf_kwargs, None))
        try:
            bookshelf_info = Bookshelf.objects.get(id=bookshelf_id)
        except IndexError:
            raise Http404
        return bookshelf_info


class BookshelfViewSet(DefaultMixin, viewsets.ModelViewSet):
    """
    API endpoint for listing and creating bookshelves.
    """
    queryset = Bookshelf.objects.order_by('name')
    serializer_class = BookshelfSerializer


class BookCollectionViewSet(DefaultMixin, viewsets.ModelViewSet):
    """
    API endpoint for listing and creating book collections.
    """
    queryset = BookCollection.objects.order_by('name')
    serializer_class = BookCollectionSerializer


class BookSeriesesView(generic.ListView):
    template_name = 'bookshelf/serieses.html'
    context_object_name = 'series_list'
    paginate_by = 20
    paginate_orphans = 5

    def get_queryset(self):
        """
        Return the author list.
        """
        return BookSeries.objects.order_by('id')


class BookSeriesView(generic.DetailView):
    model = BookSeries
    template_name = 'bookshelf/series.html'
    context_object_name = 'series'
    pk_series_kwargs = 'pk'

    def get_object(self, queryset=None):
        series_id = int(self.kwargs.get(self.pk_series_kwargs, None))
        try:
            series_info = BookSeries.objects.get(id=series_id)
        except IndexError:
            raise Http404
        return series_info


class BookSeriesViewSet(DefaultMixin, viewsets.ModelViewSet):
    """
    API endpoint for listing and creating book series.
    """
    queryset = BookSeries.objects.order_by('name')
    serializer_class = BookSeriesSerializer


class ReadingPlansView(generic.ListView):
    template_name = 'bookshelf/reading_plans.html'
    context_object_name = 'reading_plan_list'
    paginate_by = 10
    paginate_orphans = 5

    def get_queryset(self):
        """
        Return the reading plan list.
        """
        return ReadingPlan.objects.order_by('id')


class ReadingPlanView(generic.DetailView):
    model = ReadingPlan
    template_name = 'bookshelf/reading_plan.html'
    context_object_name = 'reading_plan'
    pk_plan_kwargs = 'pk'

    def get_object(self, queryset=None):
        plan_id = int(self.kwargs.get(self.pk_plan_kwargs, None))
        try:
            plan_info = ReadingPlan.objects.get(id=plan_id)
        except IndexError:
            raise Http404
        return plan_info


class ReadingPlanViewSet(DefaultMixin, viewsets.ModelViewSet):
    """
    API endpoint for listing and creating reading plan.
    """
    queryset = ReadingPlan.objects.order_by('start_date')
    serializer_class = ReadingPlanSerializer


def html_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


class BookPDFView(generic.DetailView):
    model = Book
    template_name = 'bookshelf/book.html'
    context_object_name = 'book'
    pk_book_kwarg = 'pk'

    def get(self, request, *args, **kwargs):
        book_id = int(self.kwargs.get(self.pk_book_kwarg, None))
        try:
            book_info = Book.objects.get(id=book_id)
        except IndexError:
            raise Http404
        result = {
            'book': book_info
        }
        pdf = html_to_pdf('bookshelf/bookpdf.html', result)
        return HttpResponse(pdf, content_type='application/pdf')
