from rest_framework import serializers
from .models import Project
from user.serielizers import UserSerializer
from django.contrib.auth.models import User

class ProjectSerializer(serializers.Serializer):
    
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=500)
    queryset = User.objects.all()
    user = serializers.PrimaryKeyRelatedField(queryset=queryset, many=False)
