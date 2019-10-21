from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    extern = models.BooleanField()
    count = models.IntegerField(default=0)
    count_max = models.IntegerField(default=1)

    REQUIRED_FIELDS = ['email', 'extern']

# class
