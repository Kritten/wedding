from django.conf import settings

from api.models import Game, Genre, Mood, Type


class ManagerConfig(object):
    @staticmethod
    def get_config():
        config = {
            'version': settings.VERSION,
            'paths': ManagerConfig.get_paths(),
            'count_games_total': Game.objects.count(),
            'genres': Genre.objects.all(),
            'moods': Mood.objects.all(),
            'types': Type.objects.all(),
        }

        return config

    @staticmethod
    def get_paths():
        dictionary_paths = {
            ##################################################################
            # Users
            ##################################################################
            'user': 'user',

            ##################################################################
            # Events
            ##################################################################
            'events': 'events',

            ##################################################################
            # Games
            ##################################################################
            'games': 'games',
        }

        return dictionary_paths
