from rest_framework import generics, status, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from posts.api.permissions import IsAuthorOrReadOnly
from posts.api.serializers import CommentSerializer, PostSerializer
from posts.models import Comment, Post

class PostViewSet(viewsets.ModelViewSet):
    """Provide CRUD +L functionality for Post."""
    queryset = Post.objects.all()
    lookup_field = "slug"
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentCreateAPIView(generics.CreateAPIView):
    """Allow users to Comment a Post instance if they haven't already."""
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        request_user = self.request.user
        kwarg_slug = self.kwargs.get("slug")
        post = get_object_or_404(Post, slug=kwarg_slug)

        # Raises a validation error if the user has already commented.
        if post.comments.filter(author=request_user).exists():
            raise ValidationError("You have already commented on this post!")

        serializer.save(author=request_user, post=post)


class CommentListAPIView(generics.ListAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        kwarg_slug = self.kwargs.get("slug")
        return Comment.objects.filter(post__slug=kwarg_slug).order_by("-created_at")


class CommentRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Provide *RUD functionality for a Comment instance to its author."""
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
