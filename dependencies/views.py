from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Dependency, Service
from .serializers import DependencySerializer
# Create your views here.
class DependencyViewSet(viewsets.ModelViewSet):
    queryset = Dependency.objects.all()
    serializer_class = DependencySerializer
    permission_classes = [permissions.IsAuthenticated]