

from django.conf.urls import  url
from django.urls import re_path
from django.urls import path
from rest_framework.authtoken import views
from users.views import SignupAPI

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView

)


urlpatterns = [
    url(r'^sign-up/$', SignupAPI.as_view(), name='register'),
    url(r'^token/$', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'^token/refresh/$', TokenRefreshView.as_view(), name='token_refresh'),



]