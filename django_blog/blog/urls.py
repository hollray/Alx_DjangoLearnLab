# blog/urls.py

from django.urls import path
from . import views
from .views import UserLoginView, UserLogoutView

urlpatterns = [
    # URL pattern for the registration page.
    path('register/', views.register, name='register'),

    # URL pattern for the login page, using the custom class-based view.
    path('login/', UserLoginView.as_view(), name='login'),

    # URL pattern for the logout page, using the built-in view.
    path('logout/', UserLogoutView.as_view(), name='logout'),
    
    # URL pattern for the user profile page.
    path('profile/', views.profile, name='profile'),
]
