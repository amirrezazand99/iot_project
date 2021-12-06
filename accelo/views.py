from django.shortcuts import render
from django.utils import timezone

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)

from rest_framework.generics import CreateAPIView, ListAPIView


from .api.serializers import (
    Create_accelo_record_serializer,
    ViewAcceloRecords_Serializer,
    View_filteredAccelo_serializer
)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import (
    Accelo
)
from users.models import user



# Create your views here.


class Accelo_Create_recordAPI(APIView):

    permission_classes = (IsAuthenticated,)
    serializer_class = Create_accelo_record_serializer

    def post(self, request, format=None):

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            creator = user.objects.get(username= request.user.username)
            ID_of_device = serializer.data['ID_of_device']
            x = serializer.data['x']
            y = serializer.data['y']
            z = serializer.data['z']
            roll = serializer.data['roll']
            pitch = serializer.data['pitch']
            yaw = serializer.data['yaw']
            psi = serializer.data['psi']
            theta = serializer.data['theta']
            phi = serializer.data['phi']
            labeled = serializer.data['labeled']

            try:
                new_record = Accelo(owner=creator, ID_of_device=ID_of_device, x=x, y=y,
                                    z=z, roll= roll, pitch=pitch, yaw=yaw,
                                    psi=psi, theta=theta, phi=phi,labeled=labeled)
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






class AcceloAPI_View(APIView):
    def get(self, request, format=None, *args, **kwargs):
        records = Accelo.objects.all()
        seralizer = ViewAcceloRecords_Serializer(records, many=True)

        return Response({"This is a list of all records by accelo":seralizer.data})

class AcceloFiltered_APIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = View_filteredAccelo_serializer

    def get_queryset(self):
        user = self.request.user
        return Accelo.objects.filter(owner=user)
