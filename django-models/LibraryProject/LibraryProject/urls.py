"""
URL configuration for LibraryProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from relationship_app import views as relationship_app_views


# urlpatterns = [
#    path('admin/', admin.site.urls),  # <-- default
   
#    path('', include('relationship_app.urls')),  # <-- Added this line myself
#]

urlpatterns = [
    path('admin/', admin.site.urls), # < --- Default
    path('', relationship_app_views.list_books, name='home'),
    #path('', include('relationship_app.urls')),  # <-- Added this line myself
    path('register/', relationship_app_views.register, name='register'),
#path('login/', relationship_app_views.login_view, name='login'), # Assuming login_view exists
    #path('logout/', relationship_app_views.logout_view, name='logout'), # Assuming logout_view exists
    path('list_books/', relationship_app_views.list_books, name='list_books'),
    path('admin-view/', relationship_app_views.admin_view, name='admin_view'),
    path('librarian-view/', relationship_app_views.librarian_view, name='librarian_view'),
    path('member-view/', relationship_app_views.member_view, name='member_view'),
    path('add_book/', relationship_app_views.add_book, name='add_book'),
    path('edit_book/<int:pk>/', relationship_app_views.edit_book, name='edit_book'),
    path('delete_book/<int:pk>/', relationship_app_views.delete_book, name='delete_book'),
    path('libraries/<int:pk>/', relationship_app_views.LibraryDetailView.as_view(), name='library_detail'),
]
