import factory
from factory.django import DjangoModelFactory

from app.models import Title, Country, Category


class TitleFactory(DjangoModelFactory):
    name = factory.Sequence(lambda n: 'Movie Title {}'.format(n))
    type = 'tv'
    description = factory.Sequence(lambda n: 'Description {}'.format(n))
    duration = '1 Season'
    release_year = 2020

    class Meta:
        model = Title


class CountryFactory(DjangoModelFactory):
    name = factory.Sequence(lambda n: 'Country {}'.format(n))

    class Meta:
        model = Country


class CategoryFactory(DjangoModelFactory):
    name = factory.Sequence(lambda n: 'Category {}'.format(n))

    class Meta:
        model = Category