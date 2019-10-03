from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import MethodSerializer, StatusCodeSerializer, HeaderSerializer, ServiceSerializer, GroupSerializer
from .models import Method, Header, StatusCode, Service, Group, Response

class MethodViewSet(viewsets.ModelViewSet):
    queryset = Method.objects.all()
    serializer_class = MethodSerializer
    #permission_classes = [permissions.IsAuthenticated] 

class StatusCodeViewSet(viewsets.ModelViewSet):
    queryset = StatusCode.objects.all()
    serializer_class = StatusCodeSerializer
    #permission_classes = [permissions.IsAuthenticated] 

class HeaderViewSet(viewsets.ModelViewSet):
    queryset = Header.objects.all()
    serializer_class = HeaderSerializer
    #permission_classes = [permissions.IsAuthenticated] 

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    #permission_classes = [permissions.IsAuthenticated] 

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    #permission_classes = [permissions.IsAuthenticated] 