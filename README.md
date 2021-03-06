### What is this app about?
It is a basic app that can perform operations on the database, by creating, updating, listing or deleting titles available on Netflix till 2019.
Obviously this does not have any connection with the real Netflix API, instead it creates a local database and uses some sample data from
kaggle to prepopulate the database.

### Steps to run the app:
1. Make sure you are working inside a fresh python 3.7 virtual environment. 
2. Install all the dependencies you need using `pip install -r requirements.txt`
3. Use `python manage.py migrate` to create all the tables.
4. Pre-populate the database with the management command `python manage.py prepopulate_data`
5. Run the server using `python manage.py runserver`
6. Now you can start using an API Client (like Postman) to test the APIs.

The following API's are available for use:
 - `/api/title/`: Used to Create, Read, Delete Titles.
 - `/api/country`: Used to Create or Read Countries for those titles.
 - `/api/category`: Used to Create or Read Categories for those titles.

The following query parameters are available to be used for the Title API (`/api/title`):
- `format`: The API is not using any renderer which explicitly returns data in JSON, hence it has to be specified
to get a valid response back in the API Client. Normally the format you would use is json, hence`format=json` should always be passed in a GET Request.
- `country_ids`: A comma separated list of ids of countries that you can pass to filter titles released on those countries.
- `catgegory_ids`: A comma separated list of ids of categories that you can pass to filter titles released on those categories.
- `released_year`: A year of the format `YYYY` that you can pass which will return all movies released on that particular year.


Example request:
```http request
GET http://localhost:8000/api/title/599/?format=json
```

```json
{
   "id":599,
   "name":"3%",
   "type":"tv",
   "date_added":"2021-01-29",
   "description":"In a future where the elite inhabit an island paradise far from the crowded slums, you get one chance to join the 3% saved from squalor.",
   "duration":"4 Seasons",
   "release_year":2020,
   "countries":[
      {
         "id":155,
         "name":"Brazil"
      }
   ],
   "categories":[
      {
         "id":157,
         "name":"TV Sci-Fi & Fantasy"
      },
      {
         "id":164,
         "name":"TV Dramas"
      },
      {
         "id":185,
         "name":"International TV Shows"
      }
   ]
}
```
Data source: https://www.kaggle.com/shivamb/netflix-shows