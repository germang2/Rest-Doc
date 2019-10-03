from django.urls import path, include

from .views import MethodViewSet, StatusCodeViewSet, HeaderViewSet, ServiceViewSet, GroupViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('methods', MethodViewSet)
router.register('statuscodes', StatusCodeViewSet)
router.register('headers', HeaderViewSet)
router.register('services', ServiceViewSet)
router.register('groups', GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
]