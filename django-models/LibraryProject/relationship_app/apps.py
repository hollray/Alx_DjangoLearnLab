from django.apps import AppConfig

from django.db.models.signals import post_save # Import post_save signal
from django.contrib import admin
from .models import Author, Book, Library, Librarian, UserProfile
from django.dispatch import receiver



class RelationshipAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'relationship_app'


    def ready(self):
        # Import the User model here to avoid AppRegistryNotReady error
        from django.contrib.auth.models import User
        # Import your UserProfile model here
        from .models import UserProfile

        # Define the signal receiver function within ready()
        # This ensures all apps are loaded before the signal is connected.
        @receiver(post_save, sender=User)
        def create_or_update_user_profile(sender, instance, created, **kwargs):
            """
            This signal receiver automatically creates a UserProfile for a new User.
            If the User already exists, it ensures the UserProfile is saved.
            """
            if created:
                # If a new user is created, create a corresponding UserProfile
                UserProfile.objects.create(user=instance)
            else:
                # For existing users, ensure their UserProfile is saved if it exists
                if hasattr(instance, 'userprofile'):
                    instance.userprofile.save()





@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    list_filter = ('author',)
    search_fields = ('title', 'author__name')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)