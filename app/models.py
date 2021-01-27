from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=128)


class Category(models.Model):
    name = models.CharField(max_length=128)


class Movie(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False)
    type = models.CharField(choices=('TV Show', 'Movie',), null=False, blank=False)
    date_added = models.DateField(auto_now=True)
    countries = models.ManyToManyField(Country)
    categories = models.ManyToManyField(Category)
    description = models.TextField(max_length=384)
    release_year = models.IntegerField(null=True, blank=True)




