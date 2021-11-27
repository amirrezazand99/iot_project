
from django.conf.urls import url

from django.contrib import admin

from .views import (
    Accelo_Create_recordAPI,
    AcceloAPI_View

)

urlpatterns = [
    url(r'CreateRecord/', Accelo_Create_recordAPI.as_view(), name='create_record'),
    url(r'ViewRecords/', AcceloAPI_View.as_view(), name='view_records'),

]