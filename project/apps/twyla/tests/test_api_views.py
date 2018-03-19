import json
import pytest
from datetime import datetime

from rest_framework import status
from rest_framework.test import APITestCase

from . import factories


class APIViewsetTests(APITestCase):

    """
    Testing viewset default methods
        http://www.django-rest-framework.org/api-guide/viewsets/

            list(self, request)
            create(self, request)

    """
    @classmethod
    def setUpTestData(cls):
        cls.user = factories.UserFactory.create(username="foo")
        cls.user_other = factories.UserFactory.create(username="bar")

    def setUp(self):
        self.client.force_login(self.user)
        self.book = factories.BookFactory.create(
            title="Foo",
            isbn_number="123",
        )
        self.rate = factories.RateFactory.create(
            stars=5,
            review="asdasdasdasd",
            book=self.book,
        )

    def test_create_book(self):
        response = self.client.post(
            '/api/books/',
            {
                'title': 'The Book',
                'isbn_number': '1234567',
            },
            format='json',
        )
        assert response.data['title'] == 'The Book'
        assert response.data['isbn_number'] == '1234567'
        assert response.status_code == status.HTTP_201_CREATED

    def test_list_book(self):
        response = self.client.get(
            '/api/books/',
            format='json',
        )
        results = response.data['results']
        assert results[0]['title'] == self.book.title
        assert results[0]['isbn_number'] == self.book.isbn_number
        assert response.status_code == status.HTTP_200_OK

    def test_create_rate(self):
        response = self.client.post(
            '/api/rates/',
            {
                'stars': 3,
                'review': 'awesome!',
                'book': self.book.id,
            },
            format='json',
        )
        assert response.data['stars'] == 3
        assert response.data['review'] == 'awesome!'
        assert response.data['book'] == self.book.id
        assert response.status_code == status.HTTP_201_CREATED

    def test_list_rate_of_mine_and_others_but_there_is_none(self):
        response = self.client.get(
            '/api/rates/',
            format='json',
        )
        assert response.data['results'] == []
        assert response.status_code == status.HTTP_200_OK

    def test_list_rate_of_mine_and_others_having_only_mine(self):
        self.rate_of_mine = factories.RateFactory.create(
            stars=1,
            review="foo1",
            book=self.book,
            created_by=self.user,
        )
        response = self.client.get(
            '/api/rates/',
            format='json',
        )
        results = response.data['results']
        assert results[0]['stars'] == 1
        assert results[0]['review'] == 'foo1'
        assert results[0]['book'] == self.book.id
        assert response.status_code == status.HTTP_200_OK

    def test_list_rate_of_mine_and_others_having_only_other(self):
        self.book_i_wrote = factories.BookFactory.create(
            title="Bar",
            isbn_number="444",
            created_by=self.user,
        )
        self.rate_of_other = factories.RateFactory.create(
            stars=1,
            review="foo1",
            book=self.book_i_wrote,
            created_by=self.user_other,
        )
        response = self.client.get(
            '/api/rates/',
            format='json',
        )
        results = response.data['results']
        assert results[0]['stars'] == 1
        assert results[0]['review'] == 'foo1'
        assert results[0]['book'] == self.book_i_wrote.id
        assert response.status_code == status.HTTP_200_OK

    def test_list_rate_of_mine_and_others_having_both(self):
        self.book_i_wrote = factories.BookFactory.create(
            title="Bar",
            isbn_number="444",
            created_by=self.user,
        )
        self.rate_of_mine = factories.RateFactory.create(
            stars=2,
            review="foo123",
            book=self.book,
            created_by=self.user,
        )
        self.rate_of_other = factories.RateFactory.create(
            stars=4,
            review="bar123",
            book=self.book_i_wrote,
            created_by=self.user_other,
        )
        response = self.client.get(
            '/api/rates/',
            format='json',
        )
        results = response.data['results']
        # rate of other
        assert results[0]['stars'] == 4
        assert results[0]['review'] == 'bar123'
        assert results[0]['book'] == self.book_i_wrote.id
        # rate of mine
        assert results[1]['stars'] == 2
        assert results[1]['review'] == 'foo123'
        assert results[1]['book'] == self.book.id

        assert response.status_code == status.HTTP_200_OK
