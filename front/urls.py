from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('front/', views.front, name='front'),
]