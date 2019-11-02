from rest_framework import serializers


class SerializerConfig(serializers.Serializer):
    version = serializers.CharField()
    paths = serializers.DictField()
    count_games_total = serializers.IntegerField()

    class Meta:
        fields = (
            'version',
            'paths',
            'count_games_total',
        )
