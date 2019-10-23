from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    extern = models.BooleanField()
    count = models.IntegerField(default=0)
    count_max = models.IntegerField(default=1)

    REQUIRED_FIELDS = ['email', 'extern']

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    datetime = models.DateTimeField()
    extern_only = models.BooleanField()
    location = models.TextField()
    address = models.TextField()
    icon = models.CharField(max_length=50, null=True, blank=True)
    color_icon = models.CharField(max_length=7, null=True, blank=True)
    color_background = models.CharField(max_length=7, null=True, blank=True)

