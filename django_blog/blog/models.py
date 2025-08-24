from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    """
    Represents a blog post.
    """
    # The title of the blog post, limited to 200 characters.
    title = models.CharField(max_length=200)

    # The main content of the blog post.
    content = models.TextField()

    # The date and time that the blog post was made
     # auto_now_add=True automatically sets the date when the post is first created.
    published_date = models.DateTimeField(auto_now_add=True)

     # A foreign key to the Django User model.
    # This establishes a one-to-many relationship, allowing one user to have many posts.
    # models.CASCADE ensures that if a User is deleted, all their associated posts are also deleted.
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        # This string method returns the title of the post, which is helpful
        # for displaying posts in the Django admin interface.
        return self.title
