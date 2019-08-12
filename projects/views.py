from rest_framework.views import APIView 
from .models import Project
from .serializers import ProjectSerializer
from rest_framework import authentication, permissions
from rest_framework.response import Response
from user.serielizers import UserSerializer
from rest_framework.decorators import api_view
# Create your views here.

class ListProjects(APIView):
    """
    API endpoint to retrieve all projects of the authenticate user
    """
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, format=None):
        
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)


