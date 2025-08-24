# blog/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Post

# This form extends Django's built-in UserCreationForm to include the email field.
# This makes it easy to handle both username and email during registration.
class UserRegisterForm(UserCreationForm):
    """
    A custom form for user registration.
    """
    # The email field is added here and is set to be required.
    email = forms.EmailField(required=True)

    class Meta:
        # The form is based on Django's built-in User model.
        model = User
        # It includes the standard username and password fields,
        # and now the custom email field.
        fields = ['username', 'email', 'password2', 'password2']

# This form is for updating a user's profile details later on.
class UserUpdateForm(UserChangeForm):
    """
    A custom form for updating user profile details.
    """
    # Excludes the password fields to prevent users from changing them
    # through the profile update form.
    password = None

    class Meta:
        model = User
        # The fields the user is allowed to edit are username and email.
        fields = ['username', 'email']

# A form to create and update a blog post based on the Post model.
class PostForm(forms.ModelForm):
    """
    A form for creating and updating a Post object.
    """
    class Meta:
        # The form is based on the Post model.
        model = Post
        # We include the title and content fields for the user to fill out.
        # The author will be automatically set in the view.
        fields = ['title', 'content']
