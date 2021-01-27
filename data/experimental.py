import pandas as pd

df = pd.read_csv('data.csv')

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

for index, row in df.iterrows():
    print(row['title'])

