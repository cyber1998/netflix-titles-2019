import pandas as pd
from django.core.management import BaseCommand
from progress.bar import ChargingBar

from app.models import Country, Category, Title


class Command(BaseCommand):
    help = 'This will pre-populate all data from a given csv.'

    def handle(self, *args, **options):
        # Read the csv
        df = pd.read_csv('data/data.csv')
        rows = len(df.index)

        countries = set()
        for row in df['country']:
            if type(row) != str:
                continue
            for name in row.split(","):
                countries.add(name.strip())

        categories = set()
        for row in df['listed_in']:
            if type(row) != str:
                continue
            for name in row.split(","):
                categories.add(name.strip())

        country_objects = []
        for country in countries:
            country_objects.append(Country(name=country))
        Country.objects.bulk_create(country_objects)

        category_objects = []
        for category in categories:
            category_objects.append(Category(name=category))
        Category.objects.bulk_create(category_objects)

        bar = ChargingBar('Populating data', max=rows)
        for index, row in df.iterrows():
            country_ids = []
            category_ids = []

            try:
                for country_name in row['country'].split(","):
                    country_ids.append(Country.objects.get(
                        name=country_name.strip()).id)
            # Raised in case of country field being blank
            # We could just let it pass safely
            except AttributeError:
                pass

            for category_name in row['listed_in'].split(","):
                category_ids.append(
                    Category.objects.get(
                        name=category_name.strip()
                    ).id)

            title = Title.objects.create(
                name=row['title'],
                type=row['type'],
                date_added=row['date_added'],
                release_year=row['release_year'],
                description=row['description'],
                duration=row['duration']
            )
            title.countries.set(country_ids)
            title.categories.set(category_ids)
            title.save()
            bar.next()
        bar.finish()
