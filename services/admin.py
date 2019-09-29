from django.contrib import admin
from .models import StatusCode, Response, Service, Group, Method, Header
# Register your models here.

admin.site.register(StatusCode)
admin.site.register(Response)
admin.site.register(Service)
admin.site.register(Group)
admin.site.register(Method)
admin.site.register(Header)
