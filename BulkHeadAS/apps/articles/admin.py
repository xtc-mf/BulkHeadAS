from django.contrib import admin
from . import models
admin.site.register(models.Client)
admin.site.register(models.Services)
admin.site.register(models.Employee)
admin.site.register(models.Work)
admin.site.register(models.Car)