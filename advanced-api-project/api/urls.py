# advanced_api_project/api/urls.py
from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
    # Endpoint for listing all books and applying filters/search.
    path('books/', BookListView.as_view(), name='book-list'),
    
    # Endpoint for creating a new book.
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    
    # Endpoints for retrieving, updating, and deleting a single book.
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
]