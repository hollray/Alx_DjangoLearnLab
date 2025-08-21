from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet



urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Maps to the BookList view
]