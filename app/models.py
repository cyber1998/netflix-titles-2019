from django.db import models


class Country(models.Model):
    """
    The name of the country where the title was released
    """
    name = models.CharField(max_length=128, help_text='Name of the country')

    def __str__(self):
        return self.name


class Category(models.Model):
    """
    The category in which the title was classified
    """
    name = models.CharField(max_length=128,  help_text='Name of the category')

    def __str__(self):
        return self.name


class Title(models.Model):
    """
    A title instance - contains data about the show on Netflix.
    """
    name = models.CharField(
        max_length=256,
        null=False,
        blank=False,
        help_text='Name of the title'
    )
    type = models.CharField(
        choices=[('tv', 'TV Show'), ('movie', 'Movie')],
        null=False,
        blank=False,
        max_length=10,
        help_text='The type of the title. Can be either a TV Show or a Movie'
    )
    date_added = models.DateField(
        auto_now=True,
        help_text='Date at which the movie was added to Netflix'
    )
    countries = models.ManyToManyField(
        Country,
        help_text='Specific countries where this title was released to'
    )
    categories = models.ManyToManyField(
        Category,
        help_text='The categories of the title'
    )
    description = models.TextField(
        max_length=384,
        help_text='Brief overview about the title'
    )
    # Ideally this can just be an integer field containing the number of
    # minutes, but to shorten the amount of logic, we have this
    # as a string fiel
    duration = models.CharField(
        max_length=32,
        help_text='The duration till which the title runs'
    )
    release_year = models.IntegerField(
        null=True,
        blank=True,
        help_text='The year on which this title was released'
    )

    def __str__(self):
        return self.name




