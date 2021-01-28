from rest_framework.filters import BaseFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from app.models import Title, Country, Category
from app.serializers import TitleSerializer, CountrySerializer, \
    CategorySerializer


class CustomPagination(PageNumberPagination):
    """
    Some custom pagination so as to not expose all the data at once
    """
    page_size = 10
    page_query_param = 'page'
    page_size_query_param = 'page_size'
    max_page_size = 50


class TitleFilterBackend(BaseFilterBackend):
    """
    This forms the filter backend of our Title API and will handle any
    query parameters in the API.
    """
    def filter_queryset(self, request, queryset, view):
        """
        This is a overridden method provided by the BaseFilterBackend
        to enable us to handle any filtering through query parameters,
        except pagination which is handled by it's own class.

        :param request: The request instance, which is implicitly passed
        when we include this Filter class in the filter backends attribute
        :param queryset: The queryset received from the ViewSet.
        :param view: Not used here, but we can pass it to get something
        from the view.

        :return: Queryset after filtering through all the query params.
        """
        country_ids = request.query_params.get('country_ids')

        category_ids = request.query_params.get('category_ids')

        release_year = request.query_params.get('released_year')
        if country_ids:
            queryset = queryset.filter(countries__in=country_ids.split(","))

        if category_ids:
            queryset = queryset.filter(categories__in=category_ids.split(","))

        if release_year:
            queryset = queryset.filter(release_year=release_year)

        return queryset


class TitleApiViewSet(ModelViewSet):
    """
    The basic ViewSet of the Title API. All the get, create, delete,
    post and update operations are handled in the ModelViewSet through
    their own mixins, which are already provided by Django Rest
    Framework.

    Less code = Less mistakes = Less bugs :)
    """
    # A cleaner way to filter is by creating a filter backend, and
    # passing it to the `filter_backends` attribute. Keeps the actual
    # view cleaner.

    filter_backends = [TitleFilterBackend]
    http_method_names = ['get', 'post', 'delete']

    # Adding a serializer to handle our data serialization problems.
    serializer_class = TitleSerializer
    pagination_class = CustomPagination
    queryset = Title.objects.all().order_by('id')


class CountryViewSet(ModelViewSet):
    http_method_names = ['get', 'post']
    serializer_class = CountrySerializer
    queryset = Country.objects.all().order_by('id')
    pagination_class = CustomPagination


class CategoryViewSet(ModelViewSet):
    http_method_names = ['get', 'post']
    serializer_class = CategorySerializer
    queryset = Category.objects.all().order_by('id')
    pagination_class = CustomPagination


