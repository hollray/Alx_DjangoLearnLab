# blog/urls.py

from django.urls import path
from . import views
from .views import UserLoginView, UserLogoutView, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView,PostsByTagListView


urlpatterns = [
     # --- Authentication URLs ---
    path('register/', views.register, name='register'),  # URL pattern for the registration page.
    path('login/', UserLoginView.as_view(), name='login'), # URL pattern for the login page, using the custom class-based view.
    path('logout/', UserLogoutView.as_view(), name='logout'), # URL pattern for the logout page, using the built-in view.
    path('profile/', views.profile, name='profile'),  # URL pattern for the user profile page.
    
# --- Post CRUD URLs ---
    # List all posts
    path('', PostListView.as_view(), name='blog-home'),
    # View a single post
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    # Create a new post
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    # Update an existing post
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    # Delete a post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

# --- Comment URLs ---
    path('post/<int:pk>/comment/add/', views.add_comment_to_post, name='add-comment'),
    path('comment/<int:pk>/update/', views.comment_update, name='comment-update'),
    path('comment/<int:pk>/delete/', views.comment_delete, name='comment-delete'),

    # --- Tagging and Search URLs ---
    # View posts filtered by a specific tag
    path('tags/<slug:tag_slug>/', PostsByTagListView.as_view(), name='posts-by-tag'),
    # Search functionality
    path('search/', views.search, name='search'),
]
