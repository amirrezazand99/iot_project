from django.contrib import admin
from .models import devices
from django.contrib.admin import ModelAdmin


# Register your models here.
@admin.register(devices)
class Pulse(ModelAdmin):
    fields = '__all__'
    list_display = '__all__'
