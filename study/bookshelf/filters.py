import django_filters

from .models import Publisher, Book, Author, Brand


class PublisherFilter(django_filters.rest_framework.FilterSet):
    name = django_filters.CharFilter(name='name', lookup_expr='exact')

    class Meta:
        model = Publisher
        fields = ('name',)


class BrandFilter(django_filters.rest_framework.FilterSet):
    name = django_filters.CharFilter(name='name', lookup_expr='exact')

    class Meta:
        model = Brand
        fields = ('name',)


class BookFilter(django_filters.rest_framework.FilterSet):
    isbn = django_filters.CharFilter(isbn='isbn', lookup_expr='exact')

    class Meta:
        model = Book
        fields = ('isbn',)


class AuthorFilter(django_filters.rest_framework.FilterSet):
    name = django_filters.CharFilter(name='name', lookup_expr='exact')

    class Meta:
        model = Author
        fields = ('name',)