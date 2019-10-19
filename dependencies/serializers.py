from rest_framework import serializers
from .models import Dependency

class DependencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Dependency
        fields = ['id', 'service', 'field', 'destination_service']