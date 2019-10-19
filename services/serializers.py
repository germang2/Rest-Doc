from rest_framework import serializers
from projects.models import Project
from services.models import Method, Header, StatusCode, Service, Group, Response

class StatusCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusCode
        fields = ['id', 'code', 'description']
    

class MethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Method
        fields = ['id', 'verb', 'description']

class HeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Header
        fields = ['id', 'name', 'content']

class ServiceSerializer(serializers.ModelSerializer):
    headers = serializers.StringRelatedField(many=True)
    class Meta:
        model = Service
        fields = ['id', 'name', 'description', 'end_point', 'project', 'json_data', 'method', 'headers']


class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Response
        fields = ['id', 'status_code', 'json_data', 'service']

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name', 'project', 'services', 'host', 'port']