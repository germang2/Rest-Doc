from rest_framework import serializers
from projects.models import Project
from services.models import Method, Header, StatusCode, Service, Group, Response

class StatusCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusCode
        fields = ['code', 'description']
    

class MethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Method
        fields = ['verb', 'description']

class HeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Header
        fields = ['name', 'content']

class ServiceSerializer(serializers.ModelSerializer):
    project = serializers.HyperlinkedIdentityField(
        many=False,
        view_name='project-detail'
    )
    method = serializers.StringRelatedField()
    headers = serializers.StringRelatedField(many=True)
    class Meta:
        model = Service
        fields = ['name', 'description', 'end_point', 'project', 'json_data', 'method', 'headers']

class ResponseSerializer(serializers.ModelSerializer):
    stataus_code = serializers.StringRelatedField()
    service = serializers.StringRelatedField()
    class Meta:
        model = Response
        fields = ['status_code', 'json_data', 'service']

class GroupSerializer(serializers.ModelSerializer):
    project = serializers.HyperlinkedIdentityField(
        many=False,
        view_name='project-detail'
    )
    services = serializers.HyperlinkedIdentityField(
        many=True,
        view_name='service-detail'
    )
    class Meta:
        model = Group
        fields = ['name', 'project', 'services', 'host', 'port']