from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.views import APIView
from django.utils.decorators import method_decorator
from api.classes import ManagerConfig
from api.serializers import SerializerConfig
from rest_framework.response import Response


class ViewConfig(APIView):
    @method_decorator(ensure_csrf_cookie)
    def get(self, request):
        config = ManagerConfig.get_config()

        serializer = SerializerConfig(config)

        return Response(serializer.data)
