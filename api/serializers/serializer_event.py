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
            'extern_only',
            'location',
            'address',
            'icon',
            'color_icon',
            'color_background',
        )
