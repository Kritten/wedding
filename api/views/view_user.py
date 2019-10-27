from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseBadRequest

from api.serializers.serializer_user import SerializerUser


class ViewUser(APIView):

    def get(self, request):
        serializer = SerializerUser(request.user)

        return Response(serializer.data)

    def put(self, request):
        serializer = SerializerUser(request.user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([])
def auth_login(request):
    user = authenticate(username=request.data.get('username'), password=request.data.get('password'))

    if user is not None:
        login(request._request, user)

        serializer = SerializerUser(user)

        return Response(serializer.data)
    else:
        return HttpResponseBadRequest()

@api_view(['POST'])
@permission_classes([])
def auth_logout(request):
    logout(request._request)

    return Response({})


