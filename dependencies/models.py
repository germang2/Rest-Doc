from django.db import models
from services.models import Service
# Create your models here.
class Dependency(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='service')
    field = models.CharField(max_length=100)
    destination_service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='destination_service')

    def __str__(self):
        return f'{self.service.name} - {self.name}'