# LibraryProject/urls.py
from django.contrib import admin
from django.urls import path, include
from relationship_app import views as relationship_app_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', relationship_app_views.list_books, name='home'),
    path('register/', relationship_app_views.register, name='register'),
    path('login/', relationship_app_views.login, name='login'), # Assuming login_view exists
    path('logout/', relationship_app_views.logout, name='logout'), # Assuming logout_view exists
    path('list_books/', relationship_app_views.list_books, name='list_books'),
    path('admin-view/', relationship_app_views.admin_view, name='admin_view'),
    path('librarian-view/', relationship_app_views.librarian_view, name='librarian_view'),
    path('member-view/', relationship_app_views.member_view, name='member_view'),
    path('add_book/', relationship_app_views.add_book, name='add_book'),
    path('edit_book/<int:pk>/', relationship_app_views.edit_book, name='edit_book'),
    path('delete_book/<int:pk>/', relationship_app_views.delete_book, name='delete_book'),
    path('libraries/<int:pk>/', relationship_app_views.LibraryDetailView.as_view(), name='library_detail'),
]
