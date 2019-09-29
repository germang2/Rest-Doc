from django.db import models
from projects.models import Project
from django.contrib.postgres.fields import JSONField

# Create your models here.
class StatusCode(models.Model):
    code = models.IntegerField()
    description = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return str(self.code)


class Method(models.Model):
    verb = models.CharField(max_length=12)
    description = models.CharField(max_length=100, blank=True)


class Header(models.Model):
    name = models.CharField(max_length=100)
    content = models.CharField(max_length=200)


class Service(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250, blank=True)
    end_point = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    json_data = JSONField()
    method = models.ForeignKey(Method, on_delete = models.PROTECT)
    headers = models.ManyToManyField(Header)

    def __str__(self):
        return self.name


class Response(models.Model):
    status_code = models.ForeignKey(StatusCode, on_delete=models.PROTECT)
    json_data = JSONField()
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.status_code.code)


class Group(models.Model):
    name = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    services = models.ManyToManyField(Service)
    host = models.CharField(max_length=100, blank=True)
    port = models.IntegerField()

    def __str__(self):
        return f'{self.name} - {self.project.name}'