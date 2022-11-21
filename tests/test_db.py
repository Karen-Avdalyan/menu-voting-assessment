from django.contrib.auth.models import User, Group

from restaurant.restaurantApp.menu.models import Menu
from restaurant.restaurantApp.restaurant.models import Restaurant
from restaurant.restaurantApp.utils.seed_test_db import SeedTestDB
from rest_framework.test import APITestCase


class TestDBContents(APITestCase):
    def setUp(self):
        SeedTestDB.createAll()

    def test_necessary_object_for_tests(self):
        admin, create = User.objects.get_or_create(username="adm")
        self.assertEqual(create, False, "You need to have an admin user with username 'adm'")
        self.assertEqual(admin.is_staff, True, "The user with username 'adm' should be admin")

        employee_group, create = Group.objects.get_or_create(name="employee")
        self.assertEqual(create, False, "You need to have a group with name employee")

        restaurant_group, create = Group.objects.get_or_create(name="restaurant")
        self.assertEqual(create, False, "You need to have a group with name restaurant")

        employee, create = User.objects.get_or_create(username="employee")
        self.assertEqual(create, False, "You need to have an admin user with username 'employee'")
        self.assertEqual(employee.groups.first().id, employee_group.id, "The employee user should be in group with name employee")

        restaurant_worker, create = User.objects.get_or_create(username="restaurant_worker")
        self.assertEqual(create, False, "You need to have an admin user with username 'restaurant_worker'")
        self.assertEqual(restaurant_worker.groups.first().id, restaurant_group.id,
                         "The restaurant_worker user should be in group with name restaurant")

        restaurant, create = Restaurant.objects.get_or_create(name="Ramsey's")
        self.assertEqual(create, False, "You need to have a restaurant with name 'restaurant'")
        self.assertEqual(restaurant.manager.username, "restaurant_worker", "The manager of the restaurant"
                                                                           " should be restaurant_worker")

        menus = Menu.objects.filter(name="menu")
        self.assertGreaterEqual(len(menus), 3, "You need to have at least 3 menus with name 'menu'")
