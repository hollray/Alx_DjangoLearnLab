# relationship_app/forms.py
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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
