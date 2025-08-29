# posts/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics,viewsets, permissions,status, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post, Comment,Like
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from notifications.models import Notification


class PostViewSet(viewsets.ModelViewSet):
    """
    ViewSet for handling Post-related API operations.
    Provides CRUD functionality for posts and applies search and filtering.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['author']
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        """
        Sets the author of the post to the current user upon creation.
        """
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    """
    ViewSet for handling Comment-related API operations.
    Provides CRUD functionality for comments.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        """
        Sets the author of the comment to the current user.
        """
        serializer.save(author=self.request.user)


class FeedView(ListAPIView):
    """
    API view to display a personalized feed of posts from followed users.
    """
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination

    def get_queryset(self):
        # Get the users that the current user is following
        following_users = self.request.user.following.all()
        # Return posts from those users, ordered by creation date
        queryset = Post.objects.filter(author__in=following_users).order_by('-created_at')
        return queryset
    
class LikePostView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)  
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if created:
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb='liked your post',
                target=post
            )
            return Response({'message': 'Post liked'}, status=status.HTTP_201_CREATED)
        return Response({'message': 'Already liked'}, status=status.HTTP_200_OK)


class UnlikePostView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)  
        try:
            like = Like.objects.get(user=request.user, post=post)
            like.delete()
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb='unliked your post',
                target=post
            )
            return Response({'message': 'Post unliked'}, status=status.HTTP_200_OK)
        except Like.DoesNotExist:
            return Response({'message': 'You have not liked this post'}, status=status.HTTP_400_BAD_REQUEST)