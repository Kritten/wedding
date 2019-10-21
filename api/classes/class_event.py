from typing import Tuple

from django.db.models import QuerySet
from rest_framework.request import Request

from api.classes.class_interface_manager_items import InterfaceManagerItems
from api.models import Event


class ManagerEvent(InterfaceManagerItems):
    @staticmethod
    def get_all(request: Request) -> Tuple[QuerySet, list]:
        queryset = Event.objects.all()

        queryset = ManagerEvent.sort_by(
            queryset=queryset,
            request=request
        )

        queryset, list_fields = ManagerEvent.fields(
            queryset=queryset,
            request=request,
        )

        return queryset, list_fields
