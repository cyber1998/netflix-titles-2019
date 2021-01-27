import pandas as pd

from app.models import Country, Category, Title

df = pd.read_csv('data/data.csv')

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
for category in category_objects:
    category_objects.append(Category(name=category))
Category.objects.bulk_create(category_objects)

for index, row in df.iterrows():
    Title.objects.create(
        name=row['title'],
        type=row['type'],
        date_added=row['date_added'],
        release_year=row['release_year'],

    )


