from rest_framework import serializers
from api.models import Genre


class SerializerGenre(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = (
            'id',
            'label',
        )
