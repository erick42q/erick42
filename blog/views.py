from django.shortcuts import render
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer

# Create your v# ViewSets define the view behavior.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
