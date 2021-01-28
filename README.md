### What is this app about?
It is a basic app that can perform operations on the database, by creating, updating, listing or deleting titles available on Netflix till 2019.
Obviously this does not have any connection with the real Netflix API, instead it creates a local database and uses some sample data from
kaggle to prepopulate the database.

### Steps to run the app:
1. Make sure you are working inside a fresh python 3.7 virtual environment. 
2. Install all the dependencies you need using `pip install -r requirements.txt`
3. Pre-populate the database with the management command `python manage.py prepopulate_data`
4. Run the server using `python manage.py runserver`
5. Now you can start using an API Client (like Postman) to test the APIs.

The following API's are available for use:
 - `/api/title/`: Used to Create, Read, Delete Titles.
 - `/api/country`: Used to Create or Read Countries for those titles.
 - `/api/category`: Used to Create or Read Categories for those titles.

The following query parameters are available to be used for the Title API (`/api/title`):
    - `format`: The API is not using any renderer which explicitly returns data in JSON, hence it has to be specified
    to get a valid response back in the API Client. Normally the format you would use is json, hence
    `format=json` should always be passed in a GET Request.
    - `country_ids`: A comma separated list of ids of countries that you can pass to filter titles released on those countries.
    - `catgegory_ids`: A comma separated list of ids of categories that you can pass to filter titles released on those categories.
    - `released_year`: A year of the format `YYYY` that you can pass which will return all movies released on that particular year.

Data source: https://www.kaggle.com/shivamb/netflix-shows