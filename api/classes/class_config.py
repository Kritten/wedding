from django.conf import settings

from api.models import Game


class ManagerConfig(object):
    @staticmethod
    def get_config():
        config = {
            'version': settings.VERSION,
            'paths': ManagerConfig.get_paths(),
            'count_games_total': Game.objects.count()
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
