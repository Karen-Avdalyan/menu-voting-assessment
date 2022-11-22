from django.contrib.auth.models import Group
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory

from restaurant.restaurantApp.user.employee.views import ListCreateEmployeeAPIView
from restaurant.restaurantApp.utils.seed_test_db import SeedTestDB
from tests.test_user_auth import TestUserViews


class TestRestaurantWorkerViews(APITestCase):
    @classmethod
    def setUpTestData(cls):
        SeedTestDB.createAll()

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = ListCreateEmployeeAPIView.as_view()
        self.url = reverse("user-restaurant-worker")

        Group.objects.get_or_create(name='employee')
        Group.objects.get_or_create(name='restaurant')
        self.client = TestUserViews().test_access_token()

    def test_employee_POST(self):
        post_url = reverse('user-restaurant-worker')
        resp = self.client.post(post_url, data={
            "username": "restaurant",
            "password": "12345678",
            "first_name": "test",
            "last_name": "asdf"
        })
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

    def test_employee_GET(self):
        get_url = reverse('user-restaurant-worker')
        resp = self.client.get(get_url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
