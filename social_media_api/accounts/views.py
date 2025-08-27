# accounts/views.py

from rest_framework import generics, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import get_user_model

from .serializers import UserRegistrationSerializer, UserSerializer
# Note: serializers are imported here

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    """
    API view for user registration.
    Handles user creation and returns a token upon success.
    """
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()
        Token.objects.create(user=user)

class LoginView(ObtainAuthToken):
    """
    API view for user login.
    Uses Django REST Framework's built-in ObtainAuthToken view
    to handle username/password authentication and token retrieval.
    """
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = UserSerializer(token.user).data
        return Response({'token': token.key, 'user': user})