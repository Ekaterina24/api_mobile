from rest_framework import serializers
from .models import *

class EventSerializer(serializers.ModelSerializer):
    datetime = serializers.TimeField(format="%H:%M", input_formats=['%H:%M', 'iso-8601'])

    class Meta:
        model = Event
        fields = ('id', 'agent_id', 'datetime', 'type', 'duration', 'comment')



