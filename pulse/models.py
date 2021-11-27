from django.db import models
from users.models import user

# Create your models here.

class Pulse(models.Model):
    owner = models.ForeignKey(user , on_delete = models.CASCADE , null = False)
    Device_ID = models.CharField(max_length=100 , unique=True)
    Time_send = models.DateTimeField(auto_now=True , null=False)
    HeartRate = models.CharField(max_length=100 , null = True)
    Temp = models.CharField(max_length= 100, null= True, blank= True)
    Auxiliary1 = models.CharField(max_length= 100 , null= True , blank= True)
    Auxiliary2 = models.CharField(max_length= 100 , null= True , blank= True)
    Auxiliary3 = models.CharField(max_length= 100 , null= True , blank= True)
    labeled = models.CharField(max_length=100)


