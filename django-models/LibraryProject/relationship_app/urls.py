# relationship_app/urls.py
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import RedirectView # Import RedirectView
from django.urls import reverse_lazy # Import reverse_lazy
from . import views

# This list contains the URL patterns for your app
urlpatterns = [
    path('books/', views.list_books, name='list_books'),

    # URL for user registration
    path('register/', views.register, name='register'),
    
    # URL for user login, using Django's built-in LoginView.
    # We specify the template name that this view should render.
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    
    # URL for user logout, using Django's built-in LogoutView.
    # The 'next_page' argument redirects the user after a successful logout.
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    # URL for the Admin view
    path('admin_view/', views.admin_view, name='admin_view'),
    # URL for the Librarian view
    path('librarian-dashboard/', views.librarian_view, name='librarian_view'),
    # URL for the Member view
    path('member-dashboard/', views.member_view, name='member_view'),
    
    # New URL pattern for the LibraryDetailView
    # The '<pk>' captures the primary key from the URL and passes it to the view.
    path('libraries/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # A simple home page that redirects to the login page
    # This replaces your custom login_view for the root path
    #path('', RedirectView.as_view(url=reverse_lazy('login')), name='home'),

    
    # --- New URLs for Book Permissions ---
    # path('books/add/', views.add_book, name='add_book'),
    # path('books/edit/<int:pk>/', views.edit_book, name='edit_book'),
    # path('books/delete/<int:pk>/', views.delete_book, name='delete_book'),
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),
    path('delete_book_confirm/<int:pk>/', views.delete_book, name='delete_book'),


    # A simple home page that redirects to the login page
    # This replaces your custom login_view for the root path
    path('', RedirectView.as_view(url=reverse_lazy('login')), name='home'),
]
