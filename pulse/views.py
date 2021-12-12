from django.shortcuts import render
from django.shortcuts import render
from django.utils import timezone

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)

from rest_framework.generics import CreateAPIView, ListAPIView


from .api.serializers import (
    Create_pulse_record_serializer,
    ViewPulseRecords_Serializer,
    View_filteredPulse_serializer
)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import (
    Pulse
)
from users.models import user


# Create your views here.


class Pulse_Create_recordAPI(APIView):

    permission_classes = (IsAuthenticated,)
    serializer_class = Create_pulse_record_serializer

    def post(self, request, format=None):

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            creator = user.objects.get(username= request.user.username)
            Device_ID = serializer.data['Device_ID']
            HeartRate = serializer.data['HeartRate']
            Preprocessed = serializer.data['Preprocessed']
            Temp = serializer.data['Temp']
            Auxiliary1 = serializer.data['Auxiliary1']
            Auxiliary2 = serializer.data['Auxiliary2']
            Auxiliary3 = serializer.data['Auxiliary3']
            labeled = serializer.data['labeled']

            try:
                new_record = Pulse(owner=creator, Device_ID=Device_ID, Preprocessed=Preprocessed ,
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

class PulseFiltered_APIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = View_filteredPulse_serializer

    def get_queryset(self):
        user = self.request.user
        return Pulse.objects.filter(owner=user)
