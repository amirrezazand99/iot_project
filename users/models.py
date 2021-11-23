from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator

# Create your models here.
class user(User):
    GENDER = (
        ('male','male'),
        ('female','female')
    )
    BLOODTYPE = (
        ('O','O'),
        ('A','A'),
        ('B','B'),
        ("AB","AB")


    )

    gender = models.CharField(max_length= 100 , blank = False , choices=GENDER)
    blood_type = models.CharField(max_length=100 , blank= False , choices=BLOODTYPE)
    age = models.PositiveIntegerField(null=True, blank=True)
    height = models.PositiveBigIntegerField(null=True , blank=True)
    weight = models.PositiveBigIntegerField(null=True , blank=True)


