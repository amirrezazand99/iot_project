from django.contrib.contenttypes.models import ContentType

from users.models import user

from rest_framework import serializers


class UserInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = (
             'username', 'email', 'first_name', 'last_name', 'password', 'gender', 'blood_type', 'age',
            'height', 'weight')



