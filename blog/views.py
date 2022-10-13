import json
from urllib import response

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Post
from .serializers import UserSerializer, PostSerializer


# # Create your v# ViewSets define the view behavior.
class PostViewSet(viewsets.ModelViewSet):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    queryset = Post.objects.all()
    serializer_class = PostSerializer


def indexview(request):
    return HttpResponse("pagina em construção")


class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = User.objects.all()
    serializer_class = UserSerializer


class LoginViewSet(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):

        data = json.loads(request.body)

        username = data.get("username")
        password = data.get("password")

        account = authenticate(username=username, password=password)

        print(account)

        if not account:
            return Response({"status": "password or username failed"})

        print(account.id)
        user = User.objects.get(id=account.id)

        print(user)
        return Response({"username": user.username, "status": "logged"})
