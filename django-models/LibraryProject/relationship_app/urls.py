from django.urls import path
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from .views import list_books
from .views import book_list
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

# URL for user registration
path('register/', views.register, name='register'),
    
    # URL for user login, using Django's built-in LoginView.
    # We specify the template name that this view should render.
path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    
    # URL for user logout, using Django's built-in LogoutView.
    # The 'next_page' argument redirects the user after a successful logout.
path('logout/', LogoutView.as_view(next_page='/'), name='logout'),