import json
from datetime import datetime

from rest_framework import status
from rest_framework.test import APITestCase

from . import factories

from project.apps.motius.models import Article
from django.contrib.auth.models import Permission


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

    def add_permission(self, field_name, permission_type):
        # save group
        self.group.save()
        self.group.user_set.add(self.user)
        self.group.permissions.add(
            Permission.objects.get(
                codename='{}_{}_article'.format(permission_type, field_name)
            )
        )

    @classmethod
    def setUpTestData(cls):
        cls.headers = {'content-type': 'application/json'}
        # save article
        cls.article = factories.ArticleFactory.build(
            name="Lord of the flies",
            author="William Golding",
        )
        cls.article.save()
        # save user
        cls.user = factories.UserFactory(
            username="foobar123",
            password="123",
            is_superuser=False,
            is_staff=True,
        )
        cls.user.save()
        cls.group = factories.GroupFactory(name="Guest")

    def setUp(self):
        self.client.force_login(self.user)


    def test_list_address_with_permission_for_name(self):
        self.add_permission('name', 'read')
        response = self.client.get(
            '/api/articles/',
            headers=self.headers,
        )
        results = json.loads(response.content)['results']
        assert results[0]['name'] == "Lord of the flies"
        assert 'author' not in results[0]
        assert response.status_code == status.HTTP_200_OK

    def test_list_address_with_permission_for_author(self):
        self.add_permission('author', 'read')
        response = self.client.get(
            '/api/articles/',
            headers=self.headers,
        )
        results = json.loads(response.content)['results']
        assert 'name' not in results[0]
        assert results[0]['author'] == "William Golding"
        assert response.status_code == status.HTTP_200_OK

    def test_list_address_with_permission_for_name_and_author(self):
        self.add_permission('name', 'read')
        self.add_permission('author', 'read')
        response = self.client.get(
            '/api/articles/',
            headers=self.headers,
        )
        results = json.loads(response.content)['results']
        assert results[0]['name'] == "Lord of the flies"
        assert results[0]['author'] == "William Golding"
        assert response.status_code == status.HTTP_200_OK

    def test_retrive_address(self):
        self.add_permission('name', 'read')
        self.add_permission('author', 'read')
        response = self.client.get(
            '/api/articles/{}/'.format(self.article.id),
            headers=self.headers,
        )
        assert response.data['name'] == "Lord of the flies"
        assert response.data['author'] == "William Golding"
        assert response.status_code == status.HTTP_200_OK

    def test_retrive_address_with_no_permissions(self):
        response = self.client.get(
            '/api/articles/{}/'.format(self.article.id),
            headers=self.headers,
        )
        assert response.data == {}
        assert response.status_code == status.HTTP_200_OK

    def test_create_address_without_permission_for_author(self):
        self.add_permission('name', 'change')
        response = self.client.post(
            '/api/articles/',
            {
                'name': 'Modern times',
                'author': 'Louis Ford',
            },
            headers=self.headers,
        )
        assert response.data == {'author': ['Field not allowed to change']}
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_create_address_without_permission_for_name(self):
        self.add_permission('author', 'change')
        response = self.client.post(
            '/api/articles/',
            {
                'name': 'Modern times',
                'author': 'Louis Ford',
            },
            headers=self.headers,
        )
        assert response.data == {'name': ['Field not allowed to change']}
        assert response.status_code == status.HTTP_400_BAD_REQUEST
