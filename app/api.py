from rest_framework.filters import BaseFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from app.models import Title
from app.serializers import TitleSerializer


class TitleFilterBackend(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        country_ids = request.query_params.get('country_ids')
        category_ids = request.query_params.get('category_ids')
        release_year = request.query_params.get('released_year')
        if country_ids:
            queryset.filter(countries__in=country_ids)

        if category_ids:
            queryset.filter(countries__in=category_ids)

        if release_year:
            queryset.filter(release_year=release_year)

        return queryset


class TitleApiViewSet(ModelViewSet):
    filter_backends = [TitleFilterBackend]
    http_method_names = ['get', 'post', 'delete']
    serializer_class = TitleSerializer
    pagination_class = PageNumberPagination
    queryset = Title.objects.all()
