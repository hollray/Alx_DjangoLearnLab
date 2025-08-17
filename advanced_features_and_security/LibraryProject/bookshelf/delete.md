# Delete Operation

**Command:** Delete the book you created and confirm the deletion by trying to retrieve all books again.

```python
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

