# relationship_app/views.py
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic import DetailView
from .models import Book, Library, UserProfile # Ensure all models are imported
from .forms import BookForm # Import the new BookForm
from django.http import Http404, HttpResponseForbidden # Import Http404 and HttpResponseForbidden

# Create your views here.
def list_books(request):
    """
    A function-based view that lists all books and their authors from the database.
    It returns a simple text list.
    """
    # Query all Book objects from the database
    books = Book.objects.all()

    # Pass the books to the template as context
    context = {'books': books}

    # Render the 'list_books.html' template with the context
    return render(request, 'relationship_app/list_books.html', context)


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


def register(request):
    """
    A view for user registration.
    It handles both GET and POST requests.
    """
    if request.method == 'POST':
        # If the request is POST, process the form data
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # UserProfile is created automatically by signal
            return redirect('login')
    else:
        # If the request is GET, display a blank registration form
        form = UserCreationForm()
    
    # Render the 'register.html' template with the form
    return render(request, 'relationship_app/register.html', {'form': form})


# Helper functions to check user roles
def is_admin(user):
    """ This function checks if the user has an 'Admin' Role """
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    """ This function checks if the user has a 'Librarian' Role """
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    """ This function checks if the user has a 'Member' Role """
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'


# Views with role-based access control
# The decorator ensures the user is authenticated.
@user_passes_test(lambda u: u.is_authenticated, login_url='/login/')
# @user_passes_test(is_admin, login_url='/login/')
def admin_view(request):
    """
    View accessible only to users with the 'Admin' role.
    If a non-admin user (authenticated) tries to access, they are redirected
    to their respective dashboard (Librarian or Member) or receive a 403 Forbidden.
    """
    # Check if the user is an Admin
    if is_admin(request.user):
        return render(request, 'admin_view.html', {'message': 'Welcome, Admin!'})
    elif is_librarian(request.user):
        # If not Admin, but is Librarian, redirect to Librarian dashboard
        return redirect('librarian_view')
    elif is_member(request.user):
        # If not Admin or Librarian, but is Member, redirect to Member dashboard
        return redirect('member_view')
    else:
        # If authenticated but none of the defined roles, deny access
        return HttpResponseForbidden("You do not have permission to access this page.")

@user_passes_test(is_librarian, login_url='/login/')
def librarian_view(request):
    """
    View accessible only to users with the 'Librarian' role.
    Renders 'librarian_view.html'.
    """
    return render(request, 'librarian_view.html', {'message': 'Welcome, Librarian!'})

@user_passes_test(is_member, login_url='/login/')
def member_view(request):
    """
    View accessible only to users with the 'Member' role.
    Renders 'member_view.html'.
    """
    return render(request, 'member_view.html', {'message': 'Welcome, Member!'})


# --- New Views for Book Permissions ---

@permission_required('relationship_app.can_add_book', login_url='/login/')
def add_book(request):
    """
    View to add a new book. Requires 'can_add_book' permission.
    """
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books') # Redirect to book list after adding
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form})

@permission_required('relationship_app.can_change_book', login_url='/login/')
def edit_book(request, pk):
    """
    View to edit an existing book. Requires 'can_change_book' permission.
    """
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books') # Redirect to book list after editing
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/edit_book.html', {'form': form, 'book': book})

@permission_required('relationship_app.can_delete_book', login_url='/login/')
def delete_book(request, pk):
    """
    View to delete a book. Requires 'can_delete_book' permission.
    """
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books') # Redirect to book list after deleting
    return render(request, 'relationship_app/delete_book_confirm.html', {'book': book})

