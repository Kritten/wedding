from rest_framework import serializers
from api.models import Mood


class SerializerMood(serializers.ModelSerializer):

    class Meta:
        model = Mood
        fields = (
            'id',
            'label',
        )
