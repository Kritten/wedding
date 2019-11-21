from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response

from api.helpers import paginate_queryset
from api.serializers.serializer_game import SerializerGame
from api.classes.class_game import ManagerGame


class ViewGames(APIView):
    def get(self, request):
        queryset, list_fields = ManagerGame.get_all(request=request)

        queryset_paginated, count_items = paginate_queryset(queryset, request)

        # import time
        # time.sleep(30)

        serializer = SerializerGame(
            queryset_paginated,
            many=True,
        )

        return Response({
            'items_total': count_items,
            'data': serializer.data
        })

    def post(self, request):
        ManagerGame.add(user=request.user, data=request.data)

        return Response({})
