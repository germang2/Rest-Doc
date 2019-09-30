from django.db import models
from services.models import Service
# Create your models here.
class Dependency(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    field = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.service.name} - {self.name}'