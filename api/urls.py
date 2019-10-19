from django.urls import path

from . import views

urlpatterns = [
    path('login', views.auth_login, name='login'),
    path('logout', views.auth_logout, name='logout'),
    path('user', views.ViewUser.as_view(), name='user'),
    path('config', views.ViewConfig.as_view(), name='config'),
]
