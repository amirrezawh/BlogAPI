from rest_framework import serializers
from .models import Post, PostLike, Comments

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'

class SaveLikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostLike
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comments
        fields = '__all__'