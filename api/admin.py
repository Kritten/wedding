from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class UserAdminCustom(UserAdmin):
    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Info', {
            'fields': ('extern', 'count')
        })
    )


admin.site.register(User, UserAdminCustom)
