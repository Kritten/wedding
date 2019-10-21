from rest_framework.views import APIView
from rest_framework.response import Response

from api.serializers.serializer_event import SerializerEvent
from api.classes.class_event import ManagerEvent


class ViewEvents(APIView):
    def get(self, request):
        queryset, list_fields = ManagerEvent.get_all(request=request)

        serializer = SerializerEvent(
            queryset,
            many=True,
        )

        return Response({
            'data': serializer.data
        })

