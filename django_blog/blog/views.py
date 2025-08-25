from django.shortcuts import render
from django.shortcuts import redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import UserRegisterForm, UserUpdateForm, PostForm,CommentForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import (ListView,DetailView,CreateView,UpdateView,DeleteView)
from .models import Post, User,Comment

from django.db.models import Q
from taggit.models import Tag
# Create your views here.

# The register view handles the user registration process.
def register(request):
    """
    Handles user registration.
    """
    if request.method == 'POST':
        # If the request method is POST, we process the form data.
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # If the form is valid, the user is saved.
            form.save()
            username = form.cleaned_data.get('username')
            # A success message is added to be displayed to the user.
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')  # Redirect to the login page
    else:
        # If the request is GET, we show a blank registration form.
        form = UserRegisterForm()
    
    # Render the registration page with the form.
    return render(request, 'blog/register.html', {'form': form})

# A class-based view for user login. It uses Django's built-in functionality.
class UserLoginView(LoginView):
    """
    A class-based view for user login.
    """
    template_name = 'blog/login.html'
    redirect_authenticated_user = True  # Redirects users who are already logged in

# A class-based view for user logout.
class UserLogoutView(LogoutView):
    """
    A class-based view for user logout.
    """
    template_name = 'blog/logout.html'

# This decorator ensures that only logged-in users can access the profile page.
@login_required
def profile(request):
    """
    View for displaying and updating the user's profile.
    """
    if request.method == 'POST':
        # If the request is POST, we process the update form.
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            # If the form is valid, save the changes and show a success message.
            u_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile') # Redirect to the same page to prevent POST data resubmission
    else:
        # If the request is GET, we show the form with the current user's data.
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form,
    }

    return render(request, 'blog/profile.html', context)

# A class-based view to display a list of all blog posts.
class PostListView(ListView):
    """
    Displays a list of all blog posts.
    """
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-published_date']
    paginate_by = 10

# A class-based view to display posts filtered by a specific tag.
class PostsByTagListView(ListView):
    """
    Displays a list of posts filtered by a specific tag.
    """
    model = Post
    template_name = 'blog/posts_by_tag.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        # Get the tag from the URL and filter posts by it.
        tag = get_object_or_404(Tag, slug=self.kwargs.get('tag_slug'))
        return Post.objects.filter(tags__in=[tag]).order_by('-published_date')

    def get_context_data(self, **kwargs):
        # Add the tag name to the context for use in the template.
        context = super().get_context_data(**kwargs)
        context['tag_name'] = self.kwargs.get('tag_slug')
        return context


# A class-based view to display a single blog post.
class PostDetailView(DetailView):
    """
    Displays a single blog post.
    """
    model = Post

    def get_context_data(self, **kwargs):
        # This method adds the comment form and comments to the context
        # so they can be displayed in the template.
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['comments'] = self.object.comments.order_by('-created_at')
        return context

# A class-based view to create a new blog post.
# LoginRequiredMixin ensures that only logged-in users can access this view.
class PostCreateView(LoginRequiredMixin, CreateView):
    """
    Allows a logged-in user to create a new post.
    """
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = '/'  # Redirects to the home page after creation

    # This method automatically sets the author of the post to the current user.
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# A class-based view to update an existing blog post.
# LoginRequiredMixin and UserPassesTestMixin are used for access control.
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Allows a post's author to update their post.
    """
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = '/'

    # This method checks if the current user is the author of the post.
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

# A class-based view to delete a blog post.
# Access is restricted to the post's author.
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Allows a post's author to delete their post.
    """
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = '/'

    # This method checks if the current user is the author of the post.
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
# Class-based views for comments.
class CommentCreateView(LoginRequiredMixin, CreateView):
    """
    Allows a logged-in user to create a new comment.
    """
    model = Comment
    form_class = CommentForm
    template_name = 'blog/post_detail.html'

    def form_valid(self, form):
        # Set the author and post for the comment.
        form.instance.author = self.request.user
        form.instance.post_id = self.kwargs['pk']
        messages.success(self.request, 'Your comment has been added!')
        return super().form_valid(form)

    def get_success_url(self):
        # Redirect to the post detail page after a successful comment.
        return self.object.post.get_absolute_url()


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Allows a comment's author to update their comment.
    """
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'
    
    def test_func(self):
        # Ensure only the comment's author can edit the comment.
        comment = self.get_object()
        return self.request.user == comment.author

    def get_success_url(self):
        messages.success(self.request, 'Your comment has been updated!')
        # Redirect to the post detail page after a successful update.
        return self.object.post.get_absolute_url()

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Allows a comment's author to delete their comment.
    """
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'

    def test_func(self):
        # Ensures only the comment's author can delete the comment.
        comment = self.get_object()
        return self.request.user == comment.author

    def get_success_url(self):
        messages.success(self.request, 'Your comment has been deleted!')
        # Redirect to the post detail page after a successful deletion.
        return self.object.post.get_absolute_url()

def search(request):
    """
    Handles search queries to find posts by title, content, or tags.
    """
    query = request.GET.get('q', '')
    posts = Post.objects.all().order_by('-published_date')
    if query:
        # Use Q objects to perform a complex search across multiple fields.
        posts = posts.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tags__name__icontains=query)
        ).distinct()

    context = {
        'posts': posts,
        'query': query,
    }
    return render(request, 'blog/search_results.html', context)