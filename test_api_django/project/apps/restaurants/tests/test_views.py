from datetime import datetime

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory

from . import factories


class RestaurantViewsetTests(APITestCase):

    """
    Testing viewset default methods
        http://www.django-rest-framework.org/api-guide/viewsets/

                list(self, request)
                create(self, request)
                retrieve(self, request, pk=None)
                update(self, request, pk=None)
                partial_update(self, request, pk=None)
                destroy(self, request, pk=None)

    """
    @classmethod
    def setUpTestData(cls):
        cls.client = APIRequestFactory()
        cls.headers = {'content-type': 'application/json'}
        cls.random_date = datetime(2016, 8, 4, 7, 0, 0, 0)
        cls.restaurant = factories.RestaurantFactory.build(
            name='Julio',
            opens_at=cls.random_date,
            closes_at=cls.random_date,
        )
        cls.restaurant.save()

    def test_list_address(self):
        response = self.client.get(
            '/api/restaurants/',
            headers=self.headers,
        )
        results = response.data['results']
        self.assertEqual(results[0]['name'], 'Julio')
        self.assertEqual(results[0]['opens_at'], self.random_date.isoformat())
        self.assertEqual(results[0]['closes_at'], self.random_date.isoformat())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_address(self):
        response = self.client.post(
            '/api/restaurants/',
            {
                'name': 'Allie',
                'opens_at': self.random_date,
                'closes_at': self.random_date,
            },
            headers=self.headers,
        )
        self.assertEqual(response.data['name'], 'Allie')
        self.assertEqual(
            response.data['opens_at'], self.random_date.isoformat())
        self.assertEqual(
            response.data['closes_at'], self.random_date.isoformat())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrive_address(self):
        response = self.client.get(
            '/api/restaurants/1/',
            headers=self.headers,
        )
        self.assertEqual(response.data['name'], 'Julio')
        self.assertEqual(
            response.data['opens_at'], self.random_date.isoformat())
        self.assertEqual(
            response.data['closes_at'], self.random_date.isoformat())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_address(self):
        response = self.client.put(
            '/api/restaurants/1/',
            {
                'name': 'Jose',
            },
            headers=self.headers,
        )
        self.assertEqual(response.data['name'], 'Jose')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_partial_update_address(self):
        response = self.client.patch(
            '/api/restaurants/1/',
            {'name': 'Jose2'},
            headers=self.headers,
        )
        self.assertEqual(response.data['name'], 'Jose2')
        self.assertEqual(
            response.data['opens_at'], self.random_date.isoformat())
        self.assertEqual(
            response.data['closes_at'], self.random_date.isoformat())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_destroy_address(self):
        response = self.client.delete(
            '/api/restaurants/1/',
            headers=self.headers,
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
