# router/urls.py
from django.urls import path
from .views import get_profile, get_feed, get_follow, get_notification

urlpatterns = [
    path('profile/', get_profile, name='get_profile'),
    path('feed/', get_feed, name='get_feed'),
    path('follow/', get_follow, name='get_follow'),
    path('notification/', get_notification, name='get_notification'),
]
