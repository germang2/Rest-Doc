from django.urls import path

from .views import ListProjects

urlpatterns = [
    path('projects', ListProjects.as_view(), name='projects'),
]