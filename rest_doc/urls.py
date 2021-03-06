"""rest_doc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from user.views import UserViewSet
from projects.views import ListProjects
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^api/token/$', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    re_path(r'^api/token/refresh/$', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include('projects.urls')),
    path('api/', include('services.urls')),
    path('api/', include('dependencies.urls')),
    # url(r'^api/token/verify/$', TokenVerifyView.as_view(), name='token_verify'), #url to verify token 
]