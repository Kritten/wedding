from django.db.models import QuerySet
from rest_framework.pagination import PageNumberPagination
from rest_framework.request import Request
from rest_framework.settings import api_settings

from wedding.settings import REST_FRAMEWORK


class CustomPagination(PageNumberPagination):
    page_size = REST_FRAMEWORK['PAGE_SIZE']
    page_size_query_param = REST_FRAMEWORK['PAGE_SIZE_QUERY_PARAM']

def paginate_queryset(queryset: QuerySet, request: Request):
    queryset_paginated = queryset

    if request.query_params.get(REST_FRAMEWORK['PAGE_SIZE_QUERY_PARAM']) is not None:
        paginator = api_settings.DEFAULT_PAGINATION_CLASS()
        queryset_paginated = paginator.paginate_queryset(queryset, request)
        count_items = paginator.page.paginator.count
    else:
        count_items = queryset.count()

    return queryset_paginated, count_items
