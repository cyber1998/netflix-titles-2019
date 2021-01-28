from django.test import TestCase

from app.tests.factories import CountryFactory


class CountryTestCase(TestCase):

    def setUp(self):
        self.country1 = CountryFactory()
        self.country2 = CountryFactory()

    def test_list_api(self):
        response = self.client.get('/api/country/', {'format': 'json'})
        self.assertEqual(200, response.status_code)
        self.assertEqual(2, len(response.data['results']))

    def test_get_api(self):
        response = self.client.get(
            '/api/country/{}/'.format(self.country1.pk), {'format': 'json'}
        )
        self.assertEqual(200, response.status_code)
        self.assertEqual(self.country1.name, response.data['name'])

    def test_post_api(self):
        data = {
            'name': 'Malta'
        }
        response = self.client.post('/api/country/', data)
        self.assertEqual(201, response.status_code)
        self.assertEqual(response.data['id'], 3)
        self.assertEqual(response.data['name'], data['name'])
