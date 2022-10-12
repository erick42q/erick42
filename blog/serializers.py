from rest_framework import serializers, viewsets
from .models import Post


# Serializers define the API representation.
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
