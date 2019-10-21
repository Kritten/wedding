from django.conf import settings


class ManagerConfig(object):
    @staticmethod
    def get_config():
        config = {
            'version': settings.VERSION,
            'paths': ManagerConfig.get_paths(),
        }
        return config

    @staticmethod
    def get_paths():
        dictionary_paths = {
            ##################################################################
            # User
            ##################################################################
            'user': 'user',
        }

        return dictionary_paths
