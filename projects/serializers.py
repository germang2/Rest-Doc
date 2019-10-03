from rest_framework import serializers
from .models import Project
from user.serielizers import UserSerializer
from django.contrib.auth.models import User

class ProjectSerializer(serializers.ModelSerializer):
    user = User.objects.all()
    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'user']
