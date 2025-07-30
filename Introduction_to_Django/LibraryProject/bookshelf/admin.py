# bookshelf/admin.py

from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    """
    Customizes the display and functionality of the Book model in the Django admin.
    """
    # list_display: Controls which fields are displayed on the change list page of the admin.
    list_display = ('title', 'author', 'publication_year')

    # list_filter: Enables filtering options on the right sidebar of the change list page.
    # Users can filter by these fields.
    list_filter = ('publication_year', 'author')

    # search_fields: Adds a search box to the change list page.
    # Django will search for text in these fields.
    search_fields = ('title', 'author')

    # Optional: Add a date hierarchy for date-based filtering (if you had a DateField)
    # date_hierarchy = 'publication_date'

    # Optional: Order the results in the list view
    # ordering = ('-publication_year', 'title')


# Register the Book model with the custom BookAdmin class
admin.site.register(Book, BookAdmin)

# If you only wanted to register without customization, it would be simpler:
# admin.site.register(Book)
