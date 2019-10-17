from rest_framework.views import APIView

from api.classes import ManagerConfig
from api.serializers import SerializerConfig
from rest_framework.response import Response


class Config(APIView):

    def get(self, request):
        config = ManagerConfig.get_config()

        serializer = SerializerConfig(config)

        return Response(serializer.data)
