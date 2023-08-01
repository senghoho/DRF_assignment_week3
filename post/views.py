from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework.decorators import action

from .permissions import IsOwnerOrReadOnly
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer, PostListSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    def get_serializer_class(self):
        if self.action == "list":
            return PostListSerializer
        return PostSerializer

    def get_permissions(self):
        if self.action in ["get", "create", "update", "destroy", "partial_update"]:
            return [IsAdminUser()]
        return []
    
    # 좋아요 구현
    @action(methods=["GET"], detail=True)
    def test(self, request, pk=None):
        test_post = self.get_object()
        test_post.like += 1
        test_post.save(update_fields=["like"])
        return Response()
    
    # 좋아요 상위 3개 불러오기 구현
    @action(methods=["GET"], detail=True)
    def like_list(self, request, pk=None):
        top_three_posts = Post.objects.order_by('-like')[:3]
        serializer = self.get_serializer(top_three_posts, many=True)
        return Response(serializer.data)

class CommentViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.action in ["get", "update", "destroy", "partial_update"]:
            return [IsOwnerOrReadOnly()]
        return []
    
    def get_object(self):
        obj = super().get_object()
        return obj


class PostCommentViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        post = self.kwargs.get("post_id")
        queryset = Comment.objects.filter(post_id=post)
        return queryset
    
    def get_permissions(self):
        if self.action in ["get", "create", "update", "destroy", "partial_update"]:
            return [IsAdminUser()]
        return []
        
    def create(self, request, post_id=None):
        post = get_object_or_404(Post, id=post_id)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(post=post)
        return Response(serializer.data)
