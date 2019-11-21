from django.test import TestCase, Client
from ..models import Project
from ..serializers import ProjectSerializer
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from django.urls import reverse
import json

class ProjectTest(TestCase):
    """ Test module for get all Projects """

    def setUp(self):
        url = reverse('token_obtain_pair')
        user = User.objects.create_user('test', 'test@test.com', 'secret')
        Project(
            name='Rest Doc', description='Document API Rest services', owner=user
        ).save()
        Project(
            name='TODO', description='App for TODO list', owner=user
        ).save()
        
        self.client = APIClient()
        response = self.client.post(url, {'username':'test', 'password':'secret'}, format='json')
        token = response.data["access"]
        
        #authenticate using the token header on other API
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

    def test_get_all_projects(self):
        projects = Project.objects.all()
        # get API response
        response = self.client.get(reverse('projects'))
        serializer = ProjectSerializer(projects, many=True)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer.data, response.data)