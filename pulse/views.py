from django.shortcuts import render
from django.shortcuts import render
from django.utils import timezone

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)

from rest_framework.generics import CreateAPIView


from .api.serializers import (
    Create_pulse_record_serializer,
    ViewPulseRecords_Serializer
)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import (
    Pulse
)
from users.models import user


# Create your views here.

'''
    owner = models.ForeignKey(user , on_delete = models.CASCADE , null = False)
    Device_ID = models.CharField(max_length=100 , unique=True)
    Time_send = models.DateTimeField(auto_now=True , null=False)
    HeartRate = models.CharField(max_length=100 , null = True)
    Temp = models.CharField(max_length= 100, null= True, blank= True)
    Auxiliary1 = models.CharField(max_length= 100 , null= True , blank= True)
    Auxiliary2 = models.CharField(max_length= 100 , null= True , blank= True)
    Auxiliary3 = models.CharField(max_length= 100 , null= True , blank= True)
    labeled = models.CharField(max_length=100)
'''
class Pulse_Create_recordAPI(APIView):

    permission_classes = (IsAuthenticated,)
    serializer_class = Create_pulse_record_serializer

    def post(self, request, format=None):

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            creator = user.objects.get(username= request.user.username)
            Device_ID = serializer.data['Device_ID']
            HeartRate = serializer.data['HeartRate']
            Temp = serializer.data['Temp']
            Auxiliary1 = serializer.data['Auxiliary1']
            Auxiliary2 = serializer.data['Auxiliary2']
            Auxiliary3 = serializer.data['Auxiliary3']
            labeled = serializer.data['labeled']

            try:
                new_record = Pulse(owner=creator, Device_ID=Device_ID,
                                   HeartRate=HeartRate, Temp= Temp,
                                   Auxiliary1=Auxiliary1 ,
                                   Auxiliary2= Auxiliary2,
                                   Auxiliary3= Auxiliary3,
                                   labeled= labeled)
                new_record.save()
                content = {
                    'detail': 'successfuly added the new record' }
                return Response(content, status=status.HTTP_201_CREATED)

            except:
                content = {'detail': 'Failed to add new record'}
                return Response(content, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class PulseAPI_View(APIView):
    def get(self, request, format=None, *args, **kwargs):
        records = Pulse.objects.all()
        seralizer = ViewPulseRecords_Serializer(records, many=True)

        return Response({"This is a list of all records by Pulse":seralizer.data})
