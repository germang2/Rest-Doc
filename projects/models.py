from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=False)
    colaborators = models.ManyToManyField(User, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner',)

    def __str__(self):
        return self.name