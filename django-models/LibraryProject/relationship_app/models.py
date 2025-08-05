from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Author(models.Model):
     """
    Represents an Author model with name.
    """
     name = models.CharField(max_length=200)

     

class Book(models.Model):
      """
    Represents a book with a title, author.
    """
      title = models.CharField(max_length=200)
      author = models.ForeignKey(Author,on_delete=models.CASCADE, related_name='author')

class Library(models.Model):
       """
    Represents a library model with name and books.
    """
       name = models.CharField(max_length=200)
       books = models.ManyToManyField(Book, related_name='libraries')

class Librarian(models.Model):
       """
    Represents a librarian model with a name of the librarian and the library.
    """
       name = models.CharField(max_length=200)
       library = models.OneToOneField(Library, on_delete=models.CASCADE)


# Define role choices for the UserProfile
class UserRole(models.TextChoices):
    ADMIN = 'Admin', 'Admin'
    LIBRARIAN = 'Librarian', 'Librarian'
    MEMBER = 'Member', 'Member'

class UserProfile(models.Model):
      """ Extends the Django User model to include a role for the user.
    Uses a OneToOneField to link to Django's built-in User model.
    """
      user = models.OneToOneField(User, on_delete=models.CASCADE)
      role = models.CharField(max_length=10,
                              choices=UserRole.choices,
                              default=UserRole.MEMBER, #Default Role for Users
                              help_text="User's assigned role in the system."
                              )
      
# Signal to automatically create a UserProfile when a new User is created
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender,instance,created, **kwargs):
      """
    This signal receiver automatically creates a UserProfile for a new User.
    If the User already exists, it ensures the UserProfile is saved.
    """
      if created:
            # If a new user is created, create a corresponding UserProfile
            UserProfile.objects.create(user = instance)
      # Always save the UserProfile to ensure it's updated if the User is updated
      instance.userprofile.save()

      



def __str__(self):
        """
        Returns the string representation of the Author model, which is its name.
        This is a best practice for Django models.
        """
        return self.name