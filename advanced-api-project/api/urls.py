# advanced_api_project/api/urls.py
from django.urls import path
from .views import BookListCreateView, BookDetailView

urlpatterns = [
    # URL for retrieving all books and creating a new one.
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    
    # URL for a single book, using the primary key (pk) to identify it.
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
]