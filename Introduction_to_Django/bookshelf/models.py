# bookshelf/models.py

from django.db import models


class Book(models.Model):
    """
    Represents a book with a title, author, and publication year.
    """
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        """
        Returns a string representation of the Book instance.
        """
        return f"{self.title} by {self.author} ({self.publication_year})"

    class Meta:
        """
        Meta options for the Book model.
        """
        # Optional: Define ordering or other model-specific options here
        pass
