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

    def post(self, request):
        data = {
            'name':request.data.get('name'),
            'description':request.data.get('description'),
            'owner':request.user.id
        }

        # validate if data is corrected
        serializer = ProjectSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            project_saved = serializer.save()
            context = {'success': 'Project {} has been created successfully'.format(project_saved.name)}
        else:
            context = {'error': 'Project could not be created'}

        return Response(context)
        


