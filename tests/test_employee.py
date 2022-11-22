from django.urls import reverse
from rest_framework import status

from restaurant.restaurantApp.utils.seed_test_db import SeedTestDB
from tests.test_user_auth import TestUserViews
from rest_framework.test import APITestCase


class TestEmployeeViews(APITestCase):
    @classmethod
    def setUpTestData(cls):
        SeedTestDB.createAll()

    def setUp(self):
        self.client = TestUserViews().test_access_token()

    def test_employee_POST(self):
        post_url = reverse('user-employee')
        resp = self.client.post(post_url, data={
            "username": "employee3334",
            "password": "12345678",
            "first_name": "test",
            "last_name": "asdf"
        })
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

    def test_employee_GET(self):
        get_url = reverse('user-employee')
        resp = self.client.get(get_url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
