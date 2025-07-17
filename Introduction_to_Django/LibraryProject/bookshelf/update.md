# Update Operation

**Command:** Update the title of “1984” to “Nineteen Eighty-Four” and save the changes.

```python
from bookshelf.models import Book

book = Book.objects.get(title="1984") # Retrieve the book by its current title
book.title = "Nineteen Eighty-Four" # Update the title attribute
book.save() # Save the changes to the database

print(book) # Print the updated book to confirm
