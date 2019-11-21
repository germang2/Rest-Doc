from django.test import TestCase, Client
from ..models import Service, Method
from projects.models import Project
from ..serializers import ServiceSerializer
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from django.urls import reverse
import json

class ServiceTest(TestCase):
    """ Test module for Service model """

    def setUp(self):
        user = User.objects.create_user('test', 'test@test.com', 'secret')
        url = reverse('token_obtain_pair')
        self.client = APIClient()
        response = self.client.post(url, {'username':'test', 'password':'secret'}, format='json')
        token = response.data["access"]
        
        #authenticate using the token header on other API
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        project = Project(
            name='Rest Doc', description='Document API Rest services', owner=user
        )
        project.save()

        Service(
            name='Get all resources',
            description='Returns all resources of a model',
            end_point='api/services',
            project=project,
            method=Method.objects.get(pk=1),           
        ).save()

    def test_get_services(self):
        services = Service.objects.all()
        response = self.client.get('/api/services/')
        serializer = ServiceSerializer(services, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'], serializer.data)