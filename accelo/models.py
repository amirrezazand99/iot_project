from django.db import models
from users.models import user


# Create your models here.

class Accelo(models.Model):
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
    labeled = models.CharField(max_length=100, null= True)


