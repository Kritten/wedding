from rest_framework import serializers
from api.models import Game


class SerializerGame(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = (
            'id',
            'title',
            'description',
        )
