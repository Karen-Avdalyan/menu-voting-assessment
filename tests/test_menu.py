import datetime

from django.urls import reverse
from rest_framework import status

from restaurant.restaurantApp.menu.models import Menu
from restaurant.restaurantApp.restaurant.models import Restaurant
from restaurant.restaurantApp.utils.seed_test_db import SeedTestDB
from restaurant.test_entities import TEST_ENTITIES
from tests.test_user_auth import TestUserViews
from rest_framework.test import APITestCase


class TestMenuViews(APITestCase):
    def setUp(self):
        SeedTestDB.createAll()
        self.url = reverse("menu")
        self.client = TestUserViews().test_restaurant_worker_token()
        self.employee = TestUserViews().test_employee_token()
        self.old_employee = TestUserViews().test_old_employee_token()

    def test_menu_POST(self):
        data = {
            "name": "test_menu",
            "date": datetime.date.today().strftime("%Y-%m-%d"),
            "restaurant_id": Restaurant.objects.get(name=TEST_ENTITIES["restaurant"]["name"]).id,
            "items": [
                {
                    "name": "Caesar",
                    "description": "Salad",
                    "price": "1.0"
                }
            ]
        }
        resp = self.client.post(self.url, data=data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

    def test_menu_GET(self):
        get_url = reverse('menu')
        resp = self.client.get(get_url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_menu_vote_new(self):
        vote_url = reverse('vote')
        menus = list(Menu.objects.filter(name="menu"))
        resp = self.employee.post(vote_url, data={
            "menus": [menus[0].id, menus[1].id, menus[2].id]
        }, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

    def test_menu_vote_old(self):
        vote_url = reverse('vote')
        menus = list(Menu.objects.filter(name="menu"))
        resp = self.old_employee.post(vote_url, data={
            "menu": menus[0].id
        }, format="json", **{'HTTP_BUILD_VERSION': '1.0.0', 'HTTP_USER_AGENT': 'silly-human'})
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
