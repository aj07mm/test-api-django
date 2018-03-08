from datetime import datetime

from rest_framework import status
from rest_framework.test import APITestCase

from . import factories


class ProfileViewsetTests(APITestCase):

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
        cls.headers = {'content-type': 'application/json'}
        cls.random_date = datetime(2016, 8, 4, 7, 0, 0, 0)
        cls.user = factories.UserFactory.build(
            username="foobar",
            password="123",
            is_superuser=True,
        )
        cls.user.save()
        # save profile
        cls.profile = cls.user.profile
        cls.profile.first_name='Julio',
        cls.profile.last_name='Marins',
        cls.profile.current_position='Engineer',
        cls.profile.about_you='I <3 Rio',
        cls.profile.save()

    def setUp(self):
        res = self.client.force_login(self.user)

    def test_list_address(self):
        response = self.client.get(
            '/api/profiles/',
            headers=self.headers,
        )
        results = response.data['results']
        self.assertEqual(results[0]['first_name'], 'Julio')
        self.assertEqual(results[0]['last_name'], 'Marins')
        self.assertEqual(results[0]['current_position'], 'Engineer')
        self.assertEqual(results[0]['about_you'], 'I <3 Rio')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_address(self):
        # save new user
        user = factories.UserFactory.build(username="vini")
        user.save()
        # delete profile
        user.profile.delete()
        # save profile
        response = self.client.post(
            '/api/profiles/',
            {
                'first_name': 'Vinicius',
                'last_name': 'Marins',
                'current_position': 'Engineer',
                'about_you': 'I <3 Rio',
                'user': user.id,
            },
            headers=self.headers,
        )
        self.assertEqual(response.data['first_name'], 'Vinicius')
        self.assertEqual(response.data['last_name'], 'Marins')
        self.assertEqual(response.data['current_position'], 'Engineer')
        self.assertEqual(response.data['about_you'], 'I <3 Rio')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrive_address(self):
        response = self.client.get(
            '/api/profiles/{}/'.format(self.profile.uuid),
            headers=self.headers,
        )
        self.assertEqual(response.data['first_name'], 'Julio')
        self.assertEqual(response.data['last_name'], 'Marins')
        self.assertEqual(response.data['current_position'], 'Engineer')
        self.assertEqual(response.data['about_you'], 'I <3 Rio')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_address(self):
        # save new user
        user = factories.UserFactory.build(username="camila")
        user.save()
        # delete profile
        user.profile.delete()
        # save profile
        response = self.client.put(
            '/api/profiles/{}/'.format(self.profile.uuid),
            {
                'first_name': 'Camila',
                'last_name': 'Wilson',
                'current_position': 'Producer',
                'about_you': 'I <3 SF',
                'user': user.id,
            },
            headers=self.headers,
        )
        self.assertEqual(response.data['first_name'], 'Camila')
        self.assertEqual(response.data['last_name'], 'Wilson')
        self.assertEqual(response.data['current_position'], 'Producer')
        self.assertEqual(response.data['about_you'], 'I <3 SF')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_partial_update_address(self):
        response = self.client.patch(
            '/api/profiles/{}/'.format(self.profile.uuid),
            {'first_name': 'Marcelo'},
            headers=self.headers,
        )
        self.assertEqual(response.data['first_name'], 'Marcelo')
        self.assertEqual(response.data['last_name'], 'Marins')
        self.assertEqual(response.data['current_position'], 'Engineer')
        self.assertEqual(response.data['about_you'], 'I <3 Rio')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_destroy_address(self):
        response = self.client.delete(
            '/api/profiles/{}/'.format(self.profile.uuid),
            headers=self.headers,
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
