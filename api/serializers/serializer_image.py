from rest_framework import serializers
from api.models import Image


class SerializerImage(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = (
            'id',
            'label',
            'link',
        )
