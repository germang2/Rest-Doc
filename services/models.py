from django.db import models
from projects.models import Project
from django.contrib.postgres.fields import JSONField

# Create your models here.
class StatusCode(models.Model):
    code = models.IntegerField()
    description = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f'{str(self.code)} - {self.description}'

    class Meta:
        ordering = ['code']


class Method(models.Model):
    verb = models.CharField(max_length=12)
    description = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.verb


class Header(models.Model):
    name = models.CharField(max_length=100)
    content = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}:{self.content}'

    class Meta:
        ordering = ['name']


class Service(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250, blank=True)
    end_point = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    json_data = JSONField(blank=True, null=True)
    method = models.ForeignKey(Method, on_delete = models.PROTECT)
    headers = models.ManyToManyField(Header)

    def __str__(self):
        return self.name

    """ This method returns a dict with the name of each field in the json_data
        and its corresponding type of data """
    def get_meta_data(self):
        meta_data ={}
        if self.json_data is not None:
            json = self.json_data
            for k,v in json.items():
                meta_data[k] = v
        return meta_data

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

    class Meta:
        ordering = ['name']