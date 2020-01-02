from django import template
from django.db.models import Count, Sum, Q

from api.models import User

register = template.Library()


@register.simple_tag
def get_stats():
    return User.objects.aggregate(
        count_confirmed=Sum('count'),
        count_confirmed_extern=Sum('count', filter=Q(extern=True)),
        count_confirmed_intern=Sum('count', filter=Q(extern=False)),
        count_confirmed_extern_max=Sum('count_max', filter=Q(extern=True)),
        count_confirmed_intern_max=Sum('count_max', filter=Q(extern=False)),

        count_rejected=Count('id', filter=Q(count=0)),

        count_max=Sum('count_max'),
    )
