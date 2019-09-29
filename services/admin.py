from django.contrib import admin
from .models import StatusCode, Response, Service, Group
# Register your models here.

admin.site.register(StatusCode)
admin.site.register(Response)
admin.site.register(Service)
admin.site.register(Group)
