from rest_framework import serializers
from api.models import Event


class SerializerEvent(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = (
            'id',
            'title',
            'description',
            'datetime',
            'externOnly',
            'location',
            'address',
        )
