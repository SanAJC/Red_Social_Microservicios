from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet

router = DefaultRouter()
router.register(r'user', ProfileViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]
