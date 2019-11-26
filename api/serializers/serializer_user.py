from rest_framework import serializers
from api.models import User


class SerializerUser(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'count',
            'count_max',
            'extern',
            'games_favorite',
            'filters',
            'food',
        )
