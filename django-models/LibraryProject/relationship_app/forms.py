# relationship_app/forms.py
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Book

class UserRegistrationForm(UserCreationForm):
    """
    A custom form for user registration that inherits from Django's built-in UserCreationForm.
    This form is used to handle the creation of new user accounts.
    """
    class Meta:
        # We specify that the form should be based on the User model
        model = User
        # We define the fields that the form will include
        fields = ['username', 'email']


class BookForm(forms.ModelForm):
    """
    A ModelForm for the Book model, used for creating and updating book entries.
    """
    class Meta:
        model = Book
        fields = ['title', 'author'] # Specify the fields to include in the form
