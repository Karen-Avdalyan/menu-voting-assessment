from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from restaurant.restaurantApp.user.restaurant_manager.models import RestaurantWorker
from restaurant.restaurantApp.utils.seed_test_db import SeedTestDB
from tests.test_user_auth import TestUserViews


class TestRestaurantViews(APITestCase):

    def setUp(self):
        SeedTestDB.createAll()
        self.url = reverse("restaurant")
        self.client = TestUserViews().test_access_token()

    def test_restaurant_POST(self):
        resp = self.client.post(self.url, data={
            "name": "asdf",
            "manager": RestaurantWorker.objects.first().id
        })
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

    def test_restaurant_GET(self):
        get_url = reverse('user-restaurant-worker')
        resp = self.client.get(get_url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
