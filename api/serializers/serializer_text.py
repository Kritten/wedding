from rest_framework import serializers
from api.models import Text


class SerializerText(serializers.ModelSerializer):

    class Meta:
        model = Text
        fields = (
            'label',
            'text',
        )
