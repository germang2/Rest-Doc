from rest_framework import serializers
from .models import Dependency

class DependencySerializer(serializers.ModelSerializer):
    service = serializers.HyperlinkedIdentityField(
        many=False,
        view_name='service-detail'
    )
    destination_service = serializers.HyperlinkedIdentityField(
        many=False,
        view_name='service-detail'
    )
    class Meta:
        model = Dependency
        fields = ['id', 'service', 'field', 'destination_service']