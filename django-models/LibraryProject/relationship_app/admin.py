# relationship_app/admin.py
from django.contrib import admin
from .models import Author, Book, Library, Librarian, UserProfile # Import all your models

# Register your models here so they appear in the Django admin interface.
# This allows you to manage data for these models easily.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    # You can customize the admin display for Author here
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    list_filter = ('author',)
    search_fields = ('title', 'author__name')

@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    filter_horizontal = ('books',) # Makes the many-to-many field easier to manage

@admin.register(Librarian)
class LibrarianAdmin(admin.ModelAdmin):
    list_display = ('name', 'library')
    search_fields = ('name', 'library__name')

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """
    Admin configuration for the UserProfile model.
    This allows 'role' to be managed in the Django admin.
    """
    list_display = ('user', 'role') # Display user and role in the list view
    list_filter = ('role',) # Allow filtering by role
    search_fields = ('user__username', 'role') # Allow searching by username or role

