from rest_framework import serializers


class SerializerConfig(serializers.Serializer):
    version = serializers.CharField()
    paths = serializers.DictField()

    class Meta:
        fields = (
            'version',
            'paths',
        )
