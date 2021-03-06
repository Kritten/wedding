from django.db import models
from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import truncatechars


class User(AbstractUser):
    extern = models.BooleanField()
    count = models.IntegerField(null=True, blank=True)
    count_max = models.IntegerField(default=1)
    games_favorite = models.ManyToManyField('Game', related_name='users', blank=True)
    filters = models.TextField(null=True, blank=True)
    food = models.TextField(null=True, blank=True)

    REQUIRED_FIELDS = ['email', 'extern']

    @property
    def food_short(self):
        if self.food is None:
            return '-'
        else:
            return truncatechars(self.food, 50)


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    datetime = models.DateTimeField()
    extern_only = models.BooleanField()
    address = models.TextField()
    icon = models.CharField(max_length=50, null=True, blank=True)
    color_icon = models.CharField(max_length=7, null=True, blank=True)
    color_background = models.CharField(max_length=7, null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.title


class Game(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    count_players_min = models.IntegerField(default=2)
    count_players_max = models.IntegerField(default=2)
    minutes_playtime_min = models.IntegerField()
    minutes_playtime_max = models.IntegerField()
    is_coop = models.BooleanField()
    minutes_explanation = models.IntegerField()
    genres = models.ManyToManyField('Genre', related_name='games', blank=True)
    types = models.ManyToManyField('Type', related_name='games', blank=True)
    moods = models.ManyToManyField('Mood', related_name='games', blank=True)
    images = models.ManyToManyField('Image', related_name='games', blank=True)

    def __str__(self):
        return self.title


class SuggestionGame(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey('User', on_delete=models.CASCADE)


class Genre(models.Model):
    label = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.label


class Type(models.Model):
    label = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.label


class Mood(models.Model):
    label = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.label


class Image(models.Model):
    label = models.CharField(max_length=100, unique=True)
    link = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.label


class Text(models.Model):
    label = models.CharField(max_length=100, unique=True)
    text = models.TextField()
