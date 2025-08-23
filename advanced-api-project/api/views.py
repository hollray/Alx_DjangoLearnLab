from django.shortcuts import render
from .models import Book
from rest_framework import generics, permissions,filters
from .serializers import BookSerializer
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated


# This view handles listing all books and creating a new one.
# It combines ListModelMixin for GET (list) and CreateModelMixin for POST (create).
# GenericAPIView provides the core API functionality and is a prerequisite for mixins.


# Create your views here.

class BookListCreateView(mixins.ListModelMixin,
                         mixins.CreateModelMixin,
                         generics.GenericAPIView):
    """
    Handles GET and POST requests for the Book model.
    - GET: Retrieves a list of all books.
    - POST: Creates a new book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Allow read-only access to anyone, but require authentication to create a book.
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

# This view handles retrieving, updating, and deleting a single book.
# It combines RetrieveModelMixin for GET (detail), UpdateModelMixin for PUT/PATCH,
# and DestroyModelMixin for DELETE.
class BookDetailView(mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     generics.GenericAPIView):
    """
    Handles GET, PUT/PATCH, and DELETE requests for a single Book instance.
    - GET: Retrieves a specific book by ID.
    - PUT/PATCH: Updates an existing book.
    - DELETE: Deletes an existing book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Require authentication for any of these operations.
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)    