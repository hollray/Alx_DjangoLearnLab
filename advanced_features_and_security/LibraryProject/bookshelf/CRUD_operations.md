# Django Shell CRUD Operations Documentation

This document details the commands and outputs for Create, Retrieve, Update, and Delete (CRUD) operations performed on the `Book` model within the Django shell.

---

## Create Operation

**Command:** Create a `Book` instance with the title “1984”, author “George Orwell”, and publication year 1949.

```python
from bookshelf.models import Book

book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)

# Retrieve Operation

**Command:** Retrieve and display all attributes of the book you just created.

from bookshelf.models import Book

# Assuming the book created in 'create.md' is the only one or the first one
book = Book.objects.get(title="1984")
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Publication Year: {book.publication_year}")

# To retrieve all books (useful for confirmation later)
all_books = Book.objects.all()
print("\nAll books in the database:")
for b in all_books:
    print(b)


# Update Operation

**Command:** Update the title of “1984” to “Nineteen Eighty-Four” and save the changes.


from bookshelf.models import Book

book = Book.objects.get(title="1984") # Retrieve the book by its current title
book.title = "Nineteen Eighty-Four" # Update the title attribute
book.save() # Save the changes to the database

print(book) # Print the updated book to confirm



# Delete Operation

**Command:** Delete the book you created and confirm the deletion by trying to retrieve all books again.


from bookshelf.models import Book

book = Book.objects.get(title="Nineteen Eighty-Four") # Retrieve the book by its updated title
book.delete() # Delete the book instance

# Confirm deletion by trying to retrieve all books
all_books = Book.objects.all()
print("All books after deletion:")
if not all_books:
    print("No books found.")
else:
    for b in all_books:
        print(b)

