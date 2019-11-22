from rest_framework import serializers
from api.models import Game
from api.serializers.serializer_image import SerializerImage


class SerializerGame(serializers.ModelSerializer):
    images = SerializerImage(many=True)

    class Meta:
        model = Game
        fields = (
            'id',
            'title',
            'description',
            'count_players_min',
            'count_players_max',
            'minutes_playtime_min',
            'minutes_playtime_max',
            'is_coop',
            'minutes_explanation',
            'genres',
            'types',
            'moods',
            'images',
        )
