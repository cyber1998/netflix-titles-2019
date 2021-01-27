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
    country_ids = []
    category_ids = []
    for country_name in row['country'].split(","):
        country_ids.append(Country.objects.get(name=country_name).id)

    for category_name in row['listed_in'].split(","):
        category_ids.append(Category.objects.get(name=category_name).id)

    title = Title.objects.create(
        name=row['title'],
        type=row['type'],
        date_added=row['date_added'],
        release_year=row['release_year'],
        description=row['description']
    )

    title.countries.add(country_ids)
    title.categories.add(category_ids)



