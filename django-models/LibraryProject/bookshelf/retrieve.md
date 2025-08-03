# Retrieve Operation

**Command:** Retrieve and display all attributes of the book you just created.

```python
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
