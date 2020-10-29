from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.video_feed, name='video_feed'),
    ]