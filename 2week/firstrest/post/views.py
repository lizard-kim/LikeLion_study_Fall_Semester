from django.shortcuts import render

from rest_framework import viewsets # what is viewsets?
from .models import Post
from .serializer import PostSerializer

#CBV

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer