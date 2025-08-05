from django.urls import path
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from .views import list_books
# from .views import book_list
from . import views

# This list contains the URL patterns for your app
urlpatterns = [
    # The path() function maps a URL to a view.
    # When a user navigates to '/books/', Django will call the views.list_books function.
   # path('books/', views.book_list, name='book_list'),
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
    path('admin-dashboard/', views.admin_view, name='admin_view'),
    # URL for the Librarian view
    path('librarian-dashboard/', views.librarian_view, name='librarian_view'),
    # URL for the Member view
    path('member-dashboard/', views.member_view, name='member_view'),
    
    # New URL pattern for the LibraryDetailView
    # The '<pk>' captures the primary key from the URL and passes it to the view.
    path('libraries/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

     # A simple home page or redirect for testing
    path('', views.login_view, name='home'),
]

