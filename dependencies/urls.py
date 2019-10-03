from django.urls import path, include

from .views import DependencyViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('dependencies', DependencyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]