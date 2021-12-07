
from django.conf.urls import url

from django.contrib import admin

from .views import (
    Device_Create_recordAPI,
    DeviceAPI_View,
    DeviceFiltered_APIView

)

urlpatterns = [
    url(r'CreateRecord/', Device_Create_recordAPI.as_view(), name='create_record'),
    url(r'ViewRecords/', DeviceAPI_View.as_view(), name='view_records'),
    url(r'Filtered/', DeviceFiltered_APIView.as_view(), name='filtered_view'),

]