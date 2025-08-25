from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

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

    # A manager to handle the tags for the post.
    # It allows for a many-to-many relationship with tags.
    tags = TaggableManager()


    def __str__(self):
        # This string method returns the title of the post, which is helpful
        # for displaying posts in the Django admin interface.
        return self.title
    

# A model for a comment on a blog post.
class Comment(models.Model):
    """
    Represents a comment on a blog post.
    """
    # Foreign key to the Post model, establishing a many-to-one relationship.
    # Each comment belongs to a single post.
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)

    # Foreign key to the User model, for tracking the comment's author.
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # The content of the comment.
    content = models.TextField()

    # The date and time the comment was created.
    created_at = models.DateTimeField(auto_now_add=True)

    # The date and time the comment was last updated.
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        # Returns a string representation of the comment.
        return f'Comment by {self.author} on {self.post.title}'
