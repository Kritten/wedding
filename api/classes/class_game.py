from typing import Tuple

from django.db.models import QuerySet
from rest_framework.request import Request

from api.classes.class_interface_manager_items import InterfaceManagerItems
from api.models import Game


class ManagerGame(InterfaceManagerItems):
    @staticmethod
    def get_all(request: Request) -> Tuple[QuerySet, list]:
        queryset = Game.objects.all()

        queryset = ManagerGame.sort_by(
            queryset=queryset,
            request=request
        )

        queryset, list_fields = ManagerGame.fields(
            queryset=queryset,
            request=request,
        )

        return queryset, list_fields
