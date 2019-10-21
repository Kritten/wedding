from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Event

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
            'fields': ('extern', 'count')
        }),
    )

    add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2')
        }),
        ('Info', {
            'fields': ('extern', 'count')
        }),
    )

    list_display = ('username', 'extern', 'count', 'email', 'is_staff')


class EventCustom(admin.ModelAdmin):
    list_display = ('title', 'datetime', 'externOnly')


admin.site.register(User, UserAdminCustom)
admin.site.register(Event, EventCustom)
