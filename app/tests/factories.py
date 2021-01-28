import factory
from factory.django import DjangoModelFactory

from app.models import Title, Country, Category

"""
Factories are just some code to create database objects quickly and in
a more convenient, nifty way. These are really useful to create fixtures
or similar stuff, but especially useful in tests
"""


class TitleFactory(DjangoModelFactory):
    """
    Post generation  decorator is used to populate M2M fields
    using Factory boy.Documentation Link:
    https://factoryboy.readthedocs.io/en/stable/recipes.html#simple-many-to-many-relationship
    """

    name = factory.Sequence(lambda n: 'Movie Title {}'.format(n))
    type = 'tv'
    description = factory.Sequence(lambda n: 'Description {}'.format(n))
    duration = '1 Season'
    release_year = 2020

    @factory.post_generation
    def countries(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for country in extracted:
                self.countries.add(country)

    @factory.post_generation
    def categories(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for category in extracted:
                self.categories.add(category)

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