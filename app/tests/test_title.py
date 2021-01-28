from django.test import TestCase

from app.models import Title
from app.tests.factories import CategoryFactory, CountryFactory, TitleFactory


class TitleTestCase(TestCase):

    def setUp(self):
        self.category1 = CategoryFactory()
        self.country1 = CountryFactory()
        self.title_1 = TitleFactory(countries=[self.country1], categories=[self.category1])

        self.category2 = CategoryFactory()
        self.country2 = CountryFactory()
        self.title_2 = TitleFactory(countries=[self.country2], categories=[self.category2])

    def test_list_api(self):
        response = self.client.get('/api/title/', {'format': 'json'})
        self.assertEqual(200, response.status_code)
        self.assertEqual(2, len(response.data['results']))

    def test_get_api(self):
        response = self.client.get(
            '/api/title/{}/'.format(self.title_1.pk),
            {'format': 'json'}
        )
        self.assertEqual(200, response.status_code)
        self.assertEqual(self.title_1.name, response.data['name'])
        self.assertEqual(
            self.title_1.release_year,
            response.data['release_year']
        )

    def test_post_api(self):
        data = {
            'name': 'A new movie',
            'release_year': 2021,
            'type': 'tv',
            'countries': [self.country1.pk, self.country2.pk],
            'categories': [self.category1.pk, self.category2.pk],
            'description': 'Nothing known yet',
            'duration': '1 Season',
        }
        response = self.client.post('/api/title/', data)
        self.assertEqual(201, response.status_code)
        self.assertEqual(response.data['id'], 3)
        for key, value in data.items():
            if key not in ['countries', 'categories']:
                self.assertEqual(response.data[key], data[key])

        country_data = [
            {'id': self.country1.pk, 'name': self.country1.name},
            {'id': self.country2.pk, 'name': self.country2.name}
        ]

        category_data = [
            {'id': self.category1.pk, 'name': self.category1.name},
            {'id': self.category2.pk, 'name': self.category2.name}
        ]
        self.assertEqual(response.data['countries'], country_data)
        self.assertEqual(response.data['categories'], category_data)

        # Test if the object was indeed created
        self.assertEqual(3, Title.objects.count())

    def test_delete_api(self):
        self.category3 = CategoryFactory()
        self.country3 = CountryFactory()
        title_3 = TitleFactory(countries=[self.country3],
                               categories=[self.category3])

        response = self.client.delete('/api/title/{}/'.format(title_3.pk))
        self.assertEqual(response.status_code, 204)

