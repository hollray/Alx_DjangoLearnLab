from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView
from .models import Book , Library


# Create your views here.
def book_list(request):
    """
    A function-based view that lists all books and their authors from the database.
    It returns a simple text list.
    """
    # Query all Book objects from the database
    books = Book.objects.all()

    # Create a list of strings, each containing a book's title and author
    # We use a list comprehension for a concise way to build the list
    book_titles_and_authors = [f"Title: {book.title}, Author: {book.author.name}" for book in books]

    # Join the list of strings into a single string with newlines
    response_text = "\n".join(book_titles_and_authors)

    # Return an HttpResponse with the plain text content
    return HttpResponse(response_text, content_type="text/plain")


class LibraryDetailView(DetailView):
    """
    A class-based view that displays a specific library and all its books.
    This utilizes Django's DetailView, which handles retrieving the primary object.
    """
    # Specify the model the view will be working with
    model = Library
    
    # Specify the name of the template to be used for rendering
    template_name = 'relationship_app/library_detail.html'

    def get_context_data(self, **kwargs):
        """
        This method is used to add extra context variables to the template.
        By default, DetailView provides the 'library' object. We'll add
        the related books to the context.
        """
        # Call the base implementation to get the default context
        context = super().get_context_data(**kwargs)
        
        # The 'self.object' is the Library instance retrieved by DetailView
        # We can access the related books using the reverse relationship
        context['books'] = self.object.book_set.all()
        return context
