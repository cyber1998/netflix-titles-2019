from django.db import models


class Country(models.Model):
    """
    The name of the country where the title was released
    """
    name = models.CharField(max_length=128)


class Category(models.Model):
    """
    The category in which the title was classified
    """
    name = models.CharField(max_length=128)


class Title(models.Model):
    """
    A title instance - contains data about the show on Netflix.
    """
    name = models.CharField(max_length=256, null=False, blank=False)
    type = models.CharField(choices=[
        ('tv', 'TV Show'), ('movie', 'Movie')
    ], null=False, blank=False, max_length=10)
    date_added = models.DateField(auto_now=True)
    countries = models.ManyToManyField(Country)
    categories = models.ManyToManyField(Category)
    description = models.TextField(max_length=384)
    duration = models.CharField(max_length=32)
    release_year = models.IntegerField(null=True, blank=True)




