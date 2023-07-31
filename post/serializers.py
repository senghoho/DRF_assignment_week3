from rest_framework import serializers
from .models import *

class PostSerializer(serializers.ModelSerializer):
    
    def get_comments(self, instance):
        serializer = CommentSerializer(instance.comments, many=True)
        return serializer.data

    class Meta:
        model = Post
        fields = '__all__' # 직렬화 했을 때 보여줄 필드
        read_only_field = ['id', 'created_at', 'updated_at', 'like',]

class PostListSerializer(serializers.ModelSerializer):
    comments_cnt = serializers.SerializerMethodField()

    def get_comments_cnt(self, instance):
        return instance.comments.count()
    
    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "created_at",
            "updated_at",
            "comments_cnt",
            "like",
        ]
        read_only_fields = ["id", "created_at", "updated_at", "comments_cnt"]

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__' # 직렬화 했을 때 보여줄 필드
        read_only_field = ['id', 'created_at', 'updated_at']