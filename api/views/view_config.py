from rest_framework.views import APIView
from django.utils.decorators import method_decorator
from api.classes.class_config import ManagerConfig
from api.serializers.serializer_config import SerializerConfig
from rest_framework.response import Response


class ViewConfig(APIView):
    def get(self, request):
        config = ManagerConfig.get_config()

        serializer = SerializerConfig(config)

        return Response(serializer.data)
