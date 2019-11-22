from django.urls import path

from .views import view_config, view_event, view_user, view_games

urlpatterns = [
    path('config', view_config.ViewConfig.as_view(), name='config'),

    path('login', view_user.auth_login, name='login'),
    path('logout', view_user.auth_logout, name='logout'),
    path('user', view_user.ViewUser.as_view(), name='user'),

    path('events', view_event.ViewEvents.as_view(), name='events'),

    path('games', view_games.ViewGames.as_view(), name='games'),
    path('games/set_favorite', view_games.set_favorite, name='games_set_favorite'),
]
