from django.db import models
from Users.models import NewUser


class Post(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=300)
    body = models.TextField(blank=True, default='')
    writer = models.ForeignKey(NewUser, on_delete=models.CASCADE)

class Comments(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(blank=True, default='')
    writer = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class PostLike(models.Model):
    like_user = models.ManyToManyField(NewUser)
    like_post = models.ForeignKey(Post, on_delete=models.CASCADE,
    null=True, related_name="likepost")
