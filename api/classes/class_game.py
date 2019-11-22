import json
from typing import Tuple

from django.db.models import QuerySet, Q
from rest_framework.request import Request

from api.classes.class_interface_manager_items import InterfaceManagerItems
from api.models import Game, SuggestionGame


class ManagerGame(InterfaceManagerItems):
    @staticmethod
    def get_all(request: Request) -> Tuple[QuerySet, list]:
        queryset = Game.objects.all()

        queryset = ManagerGame.filter(
            queryset=queryset,
            request=request
        )

        queryset = ManagerGame.sort_by(
            queryset=queryset,
            request=request
        )

        queryset, list_fields = ManagerGame.fields(
            queryset=queryset,
            request=request,
        )

        return queryset, list_fields


    @staticmethod
    def filter(queryset: QuerySet, request: Request) -> QuerySet:
        value = request.query_params.get('title')
        if value is not None:
            queryset = queryset.filter(Q(title__icontains=value) | Q(description__icontains=value))
                # queryset = queryset.filter(**{
                #     '{}__{}'.format(name_field, name_lookup): value
                # })

        # queryset = ManagerGame.filter_value(
        #     queryset=queryset,
        #     request=request,
        #     name_filter='title',
        #     name_field='title',
        #     name_lookup='icontains'
        # )

        queryset = ManagerGame.filter_value(
            queryset=queryset,
            request=request,
            name_filter='description',
            name_field='description',
            name_lookup='icontains'
        )

        queryset = ManagerGame.filter_value(
            queryset=queryset,
            request=request,
            name_filter='count_players_min',
            # name_field='count_players_min',
            # name_lookup='exact'
            name_field='count_players_max',
            name_lookup='gte'
        )
        queryset = ManagerGame.filter_value(
            queryset=queryset,
            request=request,
            name_filter='count_players_max',
            # name_field='count_players_max',
            name_lookup='lte',
            name_field='count_players_min'
        )

        queryset = ManagerGame.filter_value(
            queryset=queryset,
            request=request,
            name_filter='minutes_playtime_min',
            name_field='minutes_playtime_max',
            name_lookup='gte'
        )
        queryset = ManagerGame.filter_value(
            queryset=queryset,
            request=request,
            name_filter='minutes_playtime_max',
            name_field='minutes_playtime_min',
            name_lookup='lte'
        )

        queryset = ManagerGame.filter_value(
            queryset=queryset,
            request=request,
            name_filter='minutes_explanation_min',
            name_field='minutes_explanation',
            name_lookup='gte'
        )
        queryset = ManagerGame.filter_value(
            queryset=queryset,
            request=request,
            name_filter='minutes_explanation_max',
            name_field='minutes_explanation',
            name_lookup='lte'
        )

        queryset = ManagerGame.filter_boolean(
            queryset=queryset,
            request=request,
            name_filter='is_coop',
            name_field='is_coop',
        )

        queryset = ManagerGame.filter_list(
            queryset=queryset,
            request=request,
            name_filter='genres',
            name_field='genres',
        )

        queryset = ManagerGame.filter_list(
            queryset=queryset,
            request=request,
            name_filter='moods',
            name_field='moods',
        )

        queryset = ManagerGame.filter_list(
            queryset=queryset,
            request=request,
            name_filter='types',
            name_field='types',
        )
        # is_favorite
        value = request.query_params.get('is_favorite')
        if value is not None:
            if json.loads(value) is True:
                queryset = queryset.filter(users=request.user)
            else:
                queryset = queryset.exclude(users=request.user)

        return queryset

    @staticmethod
    def add(user, data):
        SuggestionGame.objects.create(
            title=data.get('title'),
            user=user
        )

    @staticmethod
    def set_favorite(request):
        if request.data.get('is_favorite'):
            request.user.games_favorite.add(request.data.get('id_game'))
        else:
            request.user.games_favorite.remove(request.data.get('id_game'))
