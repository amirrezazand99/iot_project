

from django.conf.urls import url

from django.contrib import admin

from .views import (
    Pulse_Create_recordAPI,
    PulseAPI_View,
    PulseFiltered_APIView

)


urlpatterns = [

    url(r'CreateRecord/', Pulse_Create_recordAPI.as_view(), name='create_record'),
    url(r'ViewRecords/', PulseAPI_View.as_view(), name='view_records'),
    url(r'Filtered/', PulseFiltered_APIView.as_view(), name='filtered_view'),

]