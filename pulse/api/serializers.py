from rest_framework import serializers

from users.models import user

from pulse.models import (
    Pulse
)

class Create_pulse_record_serializer(serializers.ModelSerializer):

    class Meta:
        model = Pulse
        fields = '__all__'
        extra_kwargs ={
            'owner':{'required':False},
            'Temp':{'required':False},
            'Auxiliary1': {'required':False},
            'Auxiliary2': {'required':False},
            'Auxiliary3':{'required': False},

        }

class ViewPulseRecords_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Pulse
        fields = '__all__'



class View_filteredPulse_serializer(serializers.ModelSerializer):

    class Meta:
        model = Pulse
        fields = (
            'owner',
            'Device_ID',
            'Preprocessed',
            'Time_send',
            'HeartRate',
            'Temp',
            'Auxiliary1',
            'Auxiliary2',
            'Auxiliary3',
            'labeled',
        )



