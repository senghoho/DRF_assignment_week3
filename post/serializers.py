from rest_framework import serializers
from .models import *

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__' # 직렬화 했을 때 보여줄 필드
        read_only_field = ['id', 'created_at', 'updated_at']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__' # 직렬화 했을 때 보여줄 필드
        read_only_field = ['id', 'created_at', 'updated_at']