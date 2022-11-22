from django.contrib.auth.models import User, Group

from restaurant.restaurantApp.menu.models import Menu
from restaurant.restaurantApp.restaurant.models import Restaurant
from restaurant.restaurantApp.utils.seed_test_db import SeedTestDB
from rest_framework.test import APITestCase

from restaurant.test_entities import TEST_ENTITIES


class TestDBContents(APITestCase):
    @classmethod
    def setUpTestData(cls):
        SeedTestDB.createAll()

    def test_necessary_object_for_tests(self):
        admin, create = User.objects.get_or_create(username=TEST_ENTITIES['users']['admin']['username'])
        self.assertEqual(create, False, f"You need to have an admin user with username '{TEST_ENTITIES['users']['admin']['username']}'")
        self.assertEqual(admin.is_staff, True, f"The user with username '{TEST_ENTITIES['users']['admin']['username']}' should be admin")

        employee_group, create = Group.objects.get_or_create(name=TEST_ENTITIES['groups'][0]['name'])
        self.assertEqual(create, False, f"You need to have a group with name {TEST_ENTITIES['groups'][0]['name']}")

        restaurant_group, create = Group.objects.get_or_create(name=TEST_ENTITIES['groups'][1]['name'])
        self.assertEqual(create, False, f"You need to have a group with name {TEST_ENTITIES['groups'][1]['name']}")

        employee, create = User.objects.get_or_create(username=TEST_ENTITIES['users']['employee']['username'])
        self.assertEqual(create, False, f"You need to have an admin user with username "
                                        f"'{TEST_ENTITIES['users']['admin']['username']}'")
        self.assertEqual(employee.groups.first().id, employee_group.id, f"The employee user should be in group with name "
                                                                        f"'{TEST_ENTITIES['groups'][0]['name']}'")

        restaurant_worker, create = User.objects.get_or_create(
            username=TEST_ENTITIES['users']['restaurant_worker']['username']
        )
        self.assertEqual(create, False, f"You need to have an admin user with username "
                                        f"'{TEST_ENTITIES['users']['restaurant_worker']['username']}'")
        self.assertEqual(restaurant_worker.groups.first().id, restaurant_group.id,
                         f"The restaurant_worker user should be in group with name "
                         f"{TEST_ENTITIES['groups'][1]['name']}")

        restaurant, create = Restaurant.objects.get_or_create(name=TEST_ENTITIES['restaurant']['name'])
        self.assertEqual(create, False, f"You need to have a restaurant with name "
                                        f"'{TEST_ENTITIES['restaurant']['name']}'")
        self.assertEqual(restaurant.manager.username,
                         TEST_ENTITIES['users']['restaurant_worker']['username'],
                         f"The manager of the restaurant should be "
                         f"{TEST_ENTITIES['users']['restaurant_worker']['username']}")

        menus = Menu.objects.filter(name=TEST_ENTITIES['menu']['name'])
        self.assertGreaterEqual(
            len(menus), 3, f"You need to have at least 3 menus with name '{TEST_ENTITIES['menu']['name']}'"
        )
