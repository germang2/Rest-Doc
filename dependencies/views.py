from rest_framework import viewsets, permissions
from .models import Dependency
from .serializers import DependencySerializer
# Create your views here.
class DependencyViewSet(viewsets.ModelViewSet):
    queryset = Dependency.objects.all()
    serializer_class = DependencySerializer
    #permission_classes = [permissions.IsAuthenticated]

