from django.contrib import admin
from django.utils.safestring import mark_safe
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field
from import_export.widgets import ManyToManyWidget, ForeignKeyWidget

from .models import Book, Bookshelf, Author, Publisher, BookCollection, Comment, BookSeries, ReadingPlan, MyTag, Brand


class BookshelfAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    readonly_fields = ('total_book_count', 'total_set_count', 'books')


class BookshelfResource(resources.ModelResource):
    class Meta:
        model = Bookshelf


class BookResource(resources.ModelResource):
    authors = Field(
        attribute='authors',
        widget=ManyToManyWidget(Author, field='full_name')
    )

    publisher = Field(
        # column_name='publisher_id',
        attribute='publisher',
        widget=ForeignKeyWidget(Publisher, field='name')
    )

    brand = Field(
        attribute='brand',
        widget=ForeignKeyWidget(Brand, field='name')
    )

    bookshelf = Field(
        attribute='bookshelf',
        widget=ForeignKeyWidget(Bookshelf, field='name')
    )

    class Meta:
        model = Book
        export_order = (
            'id', 'isbn', 'original_name', 'chinese_name', 'authors', 'translator', 'brand', 'publisher', 'publish_date',
            'book_series', 'binding_type', 'paper_type', 'pages', 'book_count', 'language', 'compose_type', 'price',
            'thumb_image', 'category', 'introduction', 'douban_score')
        exclude = (
            'my_comments', 'my_score', 'tags', 'purchase_price', 'purchase_date', 'registered', 'read_state',
            'bookshelf', 'link', 'edition', 'print', 'printed_number')


class BookAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    def thumb_data(self, obj):
        return mark_safe(u'<img src="%s" width="350px" />' % obj.thumb_image.url)

    def thumb_data_small(self, obj):
        return mark_safe(u'<img src="%s" width="100px" />' % obj.thumb_image.url)

    thumb_data.short_description = u'预览'
    thumb_data_small.short_description = u'预览'
    readonly_fields = ('thumb_data',)
    list_display = (
        'id', 'thumb_data_small', 'isbn', 'original_name', 'chinese_name', 'authors', 'edition', 'print', 'category',
        'purchase_date', 'read_state', 'registered', 'douban_score')
    list_filter = ['authors', 'category', 'purchase_date', 'read_state', 'registered', 'publisher', 'paper_type']
    list_per_page = 10
    search_fields = ['isbn', 'original_name', 'chinese_name', 'authors__name', 'authors__chinese_name']
    date_hierarchy = 'purchase_date'
    # filter_horizontal 在列表上添加筛选框, 直观可见
    filter_horizontal = ('authors',)
    # raw_id_fields 仅提供搜索框, 仅显示author id, 直观性不如filter_horizontal
    # raw_id_fields = ('authors', )
    autocomplete_fields = ['brand', 'publisher', 'book_series']
    ordering = ('id',)
    resource_classes = [BookResource]

    def authors(self, obj):
        return '\n'.join([author.name for author in obj.authors.all()])


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'chinese_name', 'nation', 'dynasty')
    list_filter = ['nation', 'dynasty']
    list_per_page = 20
    search_fields = ['name', 'chinese_name']


class AuthorResource(resources.ModelResource):
    class Meta:
        model = Author


class PublisherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ['name']
    list_per_page = 20
    search_fields = ['name']


class PublisherResource(resources.ModelResource):
    class Meta:
        model = Publisher


class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ['name']
    list_per_page = 20
    search_fields = ['name']


class BrandResource(resources.ModelResource):
    class Meta:
        model = Brand


class BookCollectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ['name']
    list_per_page = 20
    search_fields = ['name', 'books__original_name']
    filter_horizontal = ('books',)

    def get_books(self, obj):
        return '\n'.join([book.original_name for book in obj.books.all()])


class BookCollectionResource(resources.ModelResource):
    class Meta:
        model = BookCollection


@admin.register(BookSeries)
class BookSeriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ['name']
    list_per_page = 20
    search_fields = ['name']

    # def get_books(self, obj):
    #     return '\n'.join([book.original_name for book in obj.books.all()])


class BookSeriesResource(resources.ModelResource):
    class Meta:
        model = BookSeries


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'book', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


@admin.register(ReadingPlan)
class ReadingPlanAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'start_date', 'end_date']
    readonly_fields = ('complete_ratio',)
    list_filter = ['name', 'start_date', 'end_date']
    list_per_page = 20
    search_fields = ['name', 'books__original_name', 'books__chinese_name']
    filter_horizontal = ('books',)

    def get_books(self, obj):
        return '\n'.join([book.original_name for book in obj.books.all()])


class ReadingPlanResource(resources.ModelResource):
    class Meta:
        model = ReadingPlan


@admin.register(MyTag)
class MyTagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    list_filter = ['name']
    list_per_page = 20


class MyTagResource(resources.ModelResource):
    class Meta:
        model = MyTag


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Bookshelf, BookshelfAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(BookCollection, BookCollectionAdmin)
