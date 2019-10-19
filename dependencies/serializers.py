from rest_framework import serializers
from rest_framework.validators import ValidationError
from .models import Dependency, Service

class DependencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Dependency
        fields = ['id', 'service', 'field', 'destination_service']

    def validate_field(self, value):
        data = self.get_initial()
        field = value
        service = Service.objects.get(id=data.get('service'))
        json_data = service.json_data
        if field not in json_data:
            raise ValidationError('The associative field to the service must be exists in the json data')
        return value        