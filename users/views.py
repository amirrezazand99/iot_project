from django.shortcuts import render
from django.forms.models import model_to_dict
from django.utils import timezone

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import user
from users.api.serializers import UserInformationSerializer



# Create your views here.
'''
   gender = models.CharField(max_length= 100 , blank = False , choices=GENDER)
    blood_type = models.CharField(max_length=100 , blank= False , choices=BLOODTYPE)
    age = models.PositiveIntegerField(null=True, blank=True)
    height = models.PositiveBigIntegerField(null=True , blank=True)
    weight = models.PositiveBigIntegerField(null=True , blank=True)
'''
class SignupAPI(APIView):
    permission_classes = (AllowAny,)
    serializer_class = UserInformationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            username = serializer.data['username']
            email = serializer.data['email']
            password = serializer.data['password']
            first_name = serializer.data['first_name']
            last_name = serializer.data['last_name']
            gender = serializer.data['gender']
            blood_type = serializer.data['blood_type']
            age = serializer.data['age']
            height = serializer.data['height']
            weight = serializer.data['weight']

            try:
                new_user = user.objects.get(username=username)
                content = {'detail':
                               'This user already exists '}
                return Response(content, status=status.HTTP_400_BAD_REQUEST)

            except:

                new_user = user.objects.create_user(username=username, email=email, password=password,
                                                    first_name=first_name, last_name=last_name)

                new_user.gender = gender
                new_user.blood_type = blood_type
                new_user.age = age
                new_user.height = height
                new_user.weight= weight


                new_user.save()
                content = {'detail': 'new user successfully created ! '}

                return Response(content, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

