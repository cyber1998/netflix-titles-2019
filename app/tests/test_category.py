from django.test import TestCase

from app.tests.factories import CategoryFactory


class CategoryTestCase(TestCase):

    def setUp(self):
        self.category1 = CategoryFactory()
        self.category2 = CategoryFactory()

    def test_list_api(self):
        response = self.client.get('/api/category/', {'format': 'json'})
        self.assertEqual(200, response.status_code)
        self.assertEqual(2, len(response.data['results']))

    def test_get_api(self):
        response = self.client.get(
            '/api/category/{}/'.format(self.category1.pk), {'format': 'json'}
        )
        self.assertEqual(200, response.status_code)
        self.assertEqual(self.category1.name, response.data['name'])

    def test_post_api(self):
        data = {
            'name': 'Category 1'
        }
        response = self.client.post('/api/category/', data)
        self.assertEqual(201, response.status_code)
        self.assertEqual(response.data['id'], 3)
        self.assertEqual(response.data['name'], data['name'])
