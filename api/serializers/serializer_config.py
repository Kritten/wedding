from rest_framework import serializers

from api.serializers.serializer_genre import SerializerGenre
from api.serializers.serializer_mood import SerializerMood
from api.serializers.serializer_text import SerializerText
from api.serializers.serializer_type import SerializerType


class SerializerConfig(serializers.Serializer):
    version = serializers.CharField()
    paths = serializers.DictField()
    count_games_total = serializers.IntegerField()
    genres = SerializerGenre(many=True)
    moods = SerializerMood(many=True)
    types = SerializerType(many=True)
    texts = SerializerText(many=True)

    class Meta:
        fields = (
            'version',
            'paths',
            'count_games_total',
            'genres',
            'moods',
            'types',
            'texts',
        )
