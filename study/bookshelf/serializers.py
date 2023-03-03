from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Book, Author, Publisher, BookCollection, Bookshelf, BookSeries, ReadingPlan, Brand


class AuthorSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()

    class Meta:
        model = Author
        fields = ('id', 'name', 'chinese_name', 'nation', 'dynasty', 'intro', 'photo', 'links')

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('author-detail',
                            kwargs={'pk': obj.pk}, request=request),
        }


class BookSerializer(serializers.ModelSerializer):
    authors_display = serializers.SerializerMethodField()
    links = serializers.SerializerMethodField()
    publisher = serializers.SlugRelatedField(
        slug_field='name',
        required=True,
        allow_null=False,
        queryset=Publisher.objects.all()
    )

    class Meta:
        model = Book
        fields = (
        'id', 'isbn', 'chinese_name', 'original_name', 'authors_display', 'translator', 'publisher', 'publish_date',
        'binding_type', 'paper_type', 'pages', 'book_count', 'language', 'price', 'purchase_price',
        'purchase_date', 'thumb_image', 'link', 'category', 'introduction', 'links', 'douban_score')

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('book-detail',
                            kwargs={'pk': obj.pk}, request=request),
        }

    def get_authors_display(self, obj):
        return obj.get_authors_display()


class PublisherSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()

    class Meta:
        model = Publisher
        fields = ('id', 'name', 'introduction', 'links')

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('publisher-detail',
                            kwargs={'pk': obj.pk}, request=request)
        }


class BrandSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()

    class Meta:
        model = Brand
        fields = ('id', 'name', 'introduction', 'links')

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('brand-detail',
                            kwargs={'pk': obj.pk}, request=request)
        }


class BookCollectionSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()

    class Meta:
        model = BookCollection
        fields = ('id', 'name', 'books', 'introduction', 'links')

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('book-collection-detail',
                            kwargs={'pk': obj.pk}, request=request)
        }


class BookshelfSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()

    class Meta:
        model = Bookshelf
        fields = ('id', 'name', 'total_book_count', 'total_set_count', 'links')

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('bookshelf-detail',
                            kwargs={'pk': obj.pk}, request=request)
        }


class BookSeriesSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()

    class Meta:
        model = BookSeries
        fields = ('id', 'name', 'books', 'introduction', 'links')

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('book-series-detail',
                            kwargs={'pk': obj.pk}, request=request)
        }


class ReadingPlanSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()

    class Meta:
        model = ReadingPlan
        fields = ('id', 'name', 'description', 'start_date', 'end_date', 'books')

    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('reading-plan-detail', kwargs={'pk': obj.pk}, request=request)
        }