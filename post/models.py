from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    writer = models.CharField(max_length=50)
    content = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    # 객체가 처음 생성될 때만 값을 설정하고 이후에는 변경 X
    updated_at = models.DateTimeField(auto_now=True)
    # 객체가 저장될 때마다 값을 업데이트
    like = models.PositiveSmallIntegerField(default=0)


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, blank=False, null=False, on_delete=models.CASCADE, related_name='comments')
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    # 객체가 처음 생성될 때만 값을 설정하고 이후에는 변경 X
    updated_at = models.DateTimeField(auto_now=True)
    # 객체가 저장될 때마다 값을 업데이트