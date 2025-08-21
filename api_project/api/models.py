from django.db import models

# Create your models here.

class Book(models.Model):
    """ Book Model with just 'Title' and 'Author' fields"""
    title = models.CharField(max_length=200)
    author=models.CharField(max_length=100)
    
