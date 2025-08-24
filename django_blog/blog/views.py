from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import UserRegisterForm, UserUpdateForm, PostForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import (ListView,DetailView,CreateView,UpdateView,DeleteView)
from .models import Post, User
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


# A class-based view to display a single blog post.
class PostDetailView(DetailView):
    """
    Displays a single blog post.
    """
    model = Post

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
