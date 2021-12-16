from django.contrib import admin
from .models import Accelo
from django.contrib.admin import ModelAdmin


# Register your models here.
@admin.register(Accelo)
class Accelo(ModelAdmin):
    fields = (
    'owner', 'ID_of_device', 'x', 'y', 'z', 'roll', 'pitch', 'yaw','psi', 'theta','phi' , 'Preprocessed', 'labeled')
    list_display = (
    'owner', 'ID_of_device', 'Time_send', 'x', 'y', 'z', 'roll', 'pitch', 'yaw','psi', 'theta','phi' , 'Preprocessed', 'labeled')
'''
        owner = models.ForeignKey(user , on_delete = models.CASCADE , null = False)
    ID_of_device = models.CharField(max_length=100 , unique=True)
    Time_send = models.DateTimeField(auto_now=True , null=False)
    x = models.CharField(max_length=100)
    y = models.CharField(max_length=100)
    z = models.CharField(max_length=100)
    roll = models.CharField(max_length=100 , null = True) #nullable
    pitch = models.CharField(max_length=100 , null = True)
    yaw = models.CharField(max_length=100 , null = True)
    psi = models.CharField(max_length=100 , null=True )
    theta = models.CharField(max_length=100 , null=True)
    phi = models.CharField(max_length=100 , null=True)
    Preprocessed = models.CharField(max_length=20, null=True)
    labeled = models.CharField(max_length=100, null= True)

'''