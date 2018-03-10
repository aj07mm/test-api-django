import json
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
        # save topic
        cls.topic = factories.TopicFactory.build()
        cls.topic.save()
        # save user
        cls.user = factories.UserFactory(
            username="foobar",
            password="123",
            is_superuser=True,
            profile__first_name='Julio',
            profile__last_name='Marins',
            profile__current_position='Engineer',
            profile__about_you='I <3 Rio'
        )

    def setUp(self):
        self.client.force_login(self.user)

    def test_list_address(self):
        response = self.client.get(
            '/api/profiles/',
            headers=self.headers,
            format='json'
        )
        results = json.loads(response.content)['results']
        assert results[0]['first_name'] == 'Julio'
        assert results[0]['last_name'] == 'Marins'
        assert results[0]['current_position'] == 'Engineer'
        assert results[0]['about_you'] == 'I <3 Rio'
        assert response.status_code == status.HTTP_200_OK

    def test_retrive_address(self):
        response = self.client.get(
            '/api/profiles/{}/'.format(self.user.profile.uuid),
            headers=self.headers,
        )
        assert response.data['first_name'] == 'Julio'
        assert response.data['last_name'] == 'Marins'
        assert response.data['current_position'] == 'Engineer'
        assert response.data['about_you'] == 'I <3 Rio'
        assert response.status_code == status.HTTP_200_OK
