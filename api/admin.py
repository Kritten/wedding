from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Event, Game, Image, Genre, Mood, Type, SuggestionGame, Text

from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('extern', 'count')


class UserAdminCustom(UserAdmin):
    add_form = CustomUserCreationForm

    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Info', {
            'fields': ('extern', 'count', 'count_max')
        }),
    )

    add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2')
        }),
        ('Info', {
            'fields': ('extern', 'count', 'count_max')
        }),
    )

    list_display = ('username', 'extern', 'count', 'email', 'is_staff')


class EventCustom(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'datetime', 'extern_only')
        }),
        ('Location', {
            'fields': ('address', ('latitude', 'longitude'))
        }),
        ('Icon', {
            'fields': ('icon', 'color_icon', 'color_background')
        })
    )

    list_display = ('title', 'datetime', 'extern_only')


class GameCustom(admin.ModelAdmin):
    list_display = (
        'title',
        'count_players_min',
        'count_players_max',
        'minutes_playtime_min',
        'minutes_playtime_max',
        'is_coop',
        'minutes_explanation',
        'countFavorised'
    )
    readonly_fields = ('countFavorised',)

    def countFavorised(self, obj):
        return obj.users.count()
    # filter_horizontal = ('genres', 'types', 'images', 'moods')


class SuggestionGameCustom(admin.ModelAdmin):
    list_display = (
        'title',
    )


class TextCustom(admin.ModelAdmin):
    list_display = (
        'label',
    )


admin.site.register(User, UserAdminCustom)
admin.site.register(Event, EventCustom)
admin.site.register(Game, GameCustom)
admin.site.register(Mood)
admin.site.register(Genre)
admin.site.register(Type)
admin.site.register(Image)
admin.site.register(Text, TextCustom)
admin.site.register(SuggestionGame, SuggestionGameCustom)
