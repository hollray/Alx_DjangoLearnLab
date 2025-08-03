# Sql queries for relationship app

# Query all books by a specific author.
import os
import django

os.environ.setdefault ('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()


from relationship_app.models import Author, Book, Library, Librarian

def populate_sample_data():
    """
    Creates some sample data to query.
    This function ensures the database has data to work with
    before we run our queries.
    """
    print("Populating sample data...")
    # Clear existing data to avoid duplicates on multiple runs
    Librarian.objects.all().delete()
    Library.objects.all().delete()
    Book.objects.all().delete()
    Author.objects.all().delete()

    # Create Authors
    author1 = Author.objects.create(name="Jane Austen")
    author2 = Author.objects.create(name="George Orwell")
    author3 = Author.objects.create(name="Harper Lee")

    # Create a Library
    main_library = Library.objects.create(name="Central City Library")

    # Create a Librarian
    Librarian.objects.create(name="Ms. Davis", library=main_library)

    # Create Books
    Book.objects.create(title="Pride and Prejudice", author=author1, library=main_library)
    Book.objects.create(title="Sense and Sensibility", author=author1, library=main_library)
    Book.objects.create(title="1984", author=author2, library=main_library)
    Book.objects.create(title="Animal Farm", author=author2, library=main_library)
    Book.objects.create(title="To Kill a Mockingbird", author=author3, library=main_library)

    print("Sample data populated successfully.")

def query_books_by_author(author_name):
      # Query all books by a specific author.
    # This demonstrates a reverse relationship lookup from Author to Book.
    # """
    print(f"\n--- Querying all books by '{author_name}' ---")
    try:
        # Get the author first
        author = Author.objects.get(name=author_name)
        # using the filter method to get all books by this author
        books = Book.objects.filter(author=author)
        

        if books:
            for book in books:
                print(f"  - {book.title}")
        else:
            print(f"  - No books found for {author}.")
    except Author.DoesNotExist:
        print(f"  - Author '{author}' not found.")


def list_all_books_in_library(library_name):
    """
    List all books in a specific library.
    This demonstrates a reverse relationship lookup from Library to Book.
    """
    print(f"\n--- Listing all books in '{library_name}' ---")
    try:
        # Get the library first
        library = Library.objects.get(name=library_name)
        # Use the reverse relationship to get all books in this library
        books = library.book_set.all()

        if books:
            for book in books:
                print(f"  - {book.title} by {book.author.name}")
        else:
            print(f"  - No books found in {library_name}.")
    except Library.DoesNotExist:
        print(f"  - Library '{library_name}' not found.")


def retrieve_librarian_for_library(library_name):
    """
    Retrieve the librarian for a specific library.
    This demonstrates a forward relationship lookup from Librarian to Library.
    """
    print(f"\n--- Retrieving librarian for '{library_name}' ---")
    try:
        # Get the library
        library = Library.objects.get(name=library_name)
        # Assuming the Librarian model has a ForeignKey to Library,
        # you can query the Librarian model directly using the library object.
        librarian = Librarian.objects.get(library=library)
        print(f"  - The librarian for '{library_name}' is {librarian.name}.")
    except Library.DoesNotExist:
        print(f"  - Library '{library_name}' not found.")
    except Librarian.DoesNotExist:
        print(f"  - No librarian found for '{library_name}'.")


if __name__ == "__main__":
    """
    The main execution block of the script.
    """
    # 1. Populate the database with fresh data.
    populate_sample_data()

    # 2. Run the requested queries.
    query_books_by_author("Jane Austen")
    list_all_books_in_library("Central City Library")
    retrieve_librarian_for_library("Central City Library")

    print("\n--- Script finished. ---")
