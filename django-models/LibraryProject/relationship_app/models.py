from django.db import models

# Create your models here.
class Author (models.Model):
     """
    Represents an Author model with name.
    """
     name = models.CharField(max_length=200)

     

class Book (models.Model):
      """
    Represents a book with a title, author.
    """
      title = models.CharField(max_length=200)
      author = models.ForeignKey(Author,on_delete=models.CASCADE, related_name='author')

class Library (models.Model):
       """
    Represents a library model with name and books.
    """
       name = models.CharField(max_length=200)
       books = models.ManyToManyField(Book, related_name='libraries')

class Librarian (models.Model):
       """
    Represents a librarian model with a name of the librarian and the library.
    """
       name = models.CharField(max_length=200)
       library = models.OneToOneField(Library, on_delete=models.CASCADE)


def __str__(self):
        """
        Returns the string representation of the Author model, which is its name.
        This is a best practice for Django models.
        """
        return self.name