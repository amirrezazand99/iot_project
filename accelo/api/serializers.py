from rest_framework import serializers

from users.models import user

from accelo.models import (
    Accelo
)
class Create_accelo_record_serializer(serializers.ModelSerializer):

    class Meta:
        model = Accelo
        fields = '__all__'
        extra_kwargs ={
            'owner':{'required':False},
        }

class ViewAcceloRecords_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Accelo
        fields = '__all__'

