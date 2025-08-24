from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib.auth.views import LoginView, LogoutView

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