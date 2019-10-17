from django.urls import path

from . import views

urlpatterns = [
    path('config', views.Config.as_view(), name='config'),
]
