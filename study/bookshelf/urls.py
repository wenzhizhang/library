from django.urls import path, re_path
from rest_framework.routers import DefaultRouter
from . import views

app_name ='bookshelf'
router = DefaultRouter()
router.register(r'authors', views.AuthorViewSet)
router.register(r'books', views.BookViewSet)
router.register(r'publishers', views.PublisherViewSet)
router.register(r'bookshelves', views.BookshelfViewSet)
router.register(r'book-collections', views.BookCollectionViewSet)
router.register(r'book-serieses', views.BookSeriesViewSet)
router.register(r'reading-plans', views.ReadingPlanViewSet)
urlpatterns = [
    path('books/', views.BooksView.as_view(), name='bookshelf-books'),
    # path('books/', views.book_list, name='bookshelf-books'),
    path('books/<int:pk>/', views.BookView.as_view(), name='bookshelf-book'),
    path('books/pdf/<int:pk>/', views.BookPDFView.as_view()),
    # path('tag/<slug:tag_slug>/', views.book_list, name='book_list_by_tag'),
    path('tag/<str:tag_slug>/', views.BooksView.as_view(), name='book_list_by_tag'),
    path('authors/', views.AuthorsView.as_view(), name='bookshelf-authors'),
    path('authors/<int:pk>/', views.AuthorView.as_view(), name='bookshelf-author'),
    path('collections/', views.BookCollectionsView.as_view(), name='bookshelf-collections'),
    path('collections/<int:pk>/', views.BookCollectionView.as_view(), name='bookshelf-collection'),
    path('publishers/', views.PublishersView.as_view(), name='bookshelf-publishers'),
    path('publishers/<int:pk>/', views.PublisherView.as_view(), name='bookshelf-publisher'),
    path('brands/', views.BrandsView.as_view(), name='bookshelf-brands'),
    path('brands/<int:pk>/', views.BrandView.as_view(), name='bookshelf-brand'),
    path('serieses/', views.BookSeriesesView.as_view(), name='bookshelf-serieses'),
    path('serieses/<int:pk>/', views.BookSeriesView.as_view(), name='bookshelf-series'),
    path('books/urlsearch/<str:keywords>', views.SearchBooksView.as_view(), name='urlsearch'),
    path('books/booksearch/', views.BookSearch.as_view(), name='booksearch'),
    path('books/booksearchresult/', views.BookSearchResult.as_view(), name='booksearchresult'),
    path('plans/', views.ReadingPlansView.as_view(), name='bookshelf-plans'),
    path('plans/<int:pk>/', views.ReadingPlanView.as_view(), name='bookshelf-plan'),
    path('bookshelves/', views.BookshelvesView.as_view(), name='bookshelf-bookshelves'),
    path('bookshelves/<int:pk>', views.BookshelfView.as_view(), name='bookshelf-bookshelf'),
]