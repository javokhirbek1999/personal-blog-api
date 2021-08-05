from django.shortcuts import render, get_object_or_404

from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from rest_framework import filters

from . import serializers
from blog import models
from . import permissions


class PostList(ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = serializers.PostSerializer
    queryset = models.Post.postobjects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ['^slug']

    def get_object(self, queryset=None, **kwargs):
        slug = self.kwargs.get('pk')
        return get_object_or_404(models.Post,slug=slug)

class Comments(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.CommentSerializer

    def get_queryset(self, **kwargs):
        post = models.Post.objects.get(slug=self.kwargs.get('pk'))
        return models.allComments(post)

class Replies(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.ReplySerializer

    def get_queryset(self, **kwargs):
        comment = models.Comment.objects.get(id=self.kwargs.get('pk'))
        return models.allReplies(comment)