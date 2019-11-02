from rest_framework import serializers
from api.models import Type


class SerializerType(serializers.ModelSerializer):

    class Meta:
        model = Type
        fields = (
            'id',
            'label',
        )
