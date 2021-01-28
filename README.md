### What is this app about?
It is a basic app that can perform operations on the database, by creating, listing or deleting titles available on Netflix till 2019.
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


Data source: https://www.kaggle.com/shivamb/netflix-shows