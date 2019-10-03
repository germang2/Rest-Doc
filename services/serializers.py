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
    project = serializers.PrimaryKeyRelatedField(
        read_only=True
    )
    method = serializers.StringRelatedField()
    headers = serializers.StringRelatedField(many=True)
    class Meta:
        model = Service
        fields = ['id', 'name', 'description', 'end_point', 'project', 'json_data', 'method', 'headers']

class ResponseSerializer(serializers.ModelSerializer):
    stataus_code = serializers.StringRelatedField()
    service = serializers.StringRelatedField()
    class Meta:
        model = Response
        fields = ['id', 'status_code', 'json_data', 'service']

class GroupSerializer(serializers.ModelSerializer):
    project = serializers.PrimaryKeyRelatedField(
        read_only=True
    )
    services = serializers.PrimaryKeyRelatedField(
        read_only=True
    ) 
    class Meta:
        model = Group
        fields = ['id', 'name', 'project', 'services', 'host', 'port']