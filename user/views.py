from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from django.shortcuts import get_object_or_404
from .serielizers import UserSerializer
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    permission_classes = [permissions.IsAuthenticated]