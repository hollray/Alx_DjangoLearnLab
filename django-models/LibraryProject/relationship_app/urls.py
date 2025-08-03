from django.urls import path
from . import views

# This list contains the URL patterns for your app
urlpatterns = [
    # The path() function maps a URL to a view.
    # When a user navigates to '/books/', Django will call the views.book_list function.
    path('books/', views.book_list, name='book_list'),
    
    # New URL pattern for the LibraryDetailView
    # The '<pk>' captures the primary key from the URL and passes it to the view.
    path('libraries/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]
