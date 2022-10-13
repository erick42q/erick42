from rest_framework import serializers, viewsets
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Post


# Serializers define the API representation.
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "is_staff"]
