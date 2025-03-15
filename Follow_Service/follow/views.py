from rest_framework import viewsets
from .models import Follow
from .serializer import FollowSerializer

class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
