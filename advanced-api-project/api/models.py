""" This model is for the API app and sepcification is strickly followed as instructed by ALX
it contains the following:

- An Author model having only name field
- A Book model having title, publication_year and author fields. The author field is a foreingKey linikng to the Author table(model)"""

from django.db import models



# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name
    

class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title
    

