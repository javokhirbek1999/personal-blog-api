from rest_framework import serializers

from blog.models import Post, Category, Comment, Reply


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','category','title','thumbnail','slug','content','published','likes','dislikes','status')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','name')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id','user','post','body','posted')


class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ('id','user','body','comment','posted')
