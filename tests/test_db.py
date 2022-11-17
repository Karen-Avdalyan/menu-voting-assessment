from django.contrib.auth.models import User, Group
from rest_framework.test import APITestCase

from restaurant.restaurantApp.menu.models import Menu
from restaurant.restaurantApp.restaurant.models import Restaurant


class TestDBContents(APITestCase):
    def test_necessary_object_for_tests(self):
        admin, create = User.objects.get_or_create(username="adm")
        self.assertEqual(create, False, "You need to have an admin user with username 'adm'")
        self.assertEqual(admin.is_staff, True, "The user with username 'adm' should be admin")

        employee_group, create = Group.objects.get_or_create(pk=1)
        self.assertEqual(create, False, "You need to have a group with id 1")

        employee_group, create = Group.objects.get_or_create(pk=2)
        self.assertEqual(create, False, "You need to have a group with id 2")

        employee, create = User.objects.get_or_create(username="employee")
        self.assertEqual(create, False, "You need to have an admin user with username 'employee'")
        self.assertEqual(employee.groups.first().id, 1, "The employee user should be in group with id 1")

        restaurant_worker, create = User.objects.get_or_create(username="restaurant_worker")
        self.assertEqual(create, False, "You need to have an admin user with username 'restaurant_worker'")
        self.assertEqual(restaurant_worker.groups.first().id, 2, "The restaurant_worker user should be in group with id 2")

        restaurant, create = Restaurant.objects.get_or_create(name="restaurant")
        self.assertEqual(create, False, "You need to have a restaurant with name 'restaurant'")
        self.assertEqual(restaurant.manager.username, "restaurant_worker", "The manager of the restaurant"
                                                                           " should be restaurant_worker")

        menus = Menu.objects.filter(name="menu")
        self.assertGreaterEqual(len(menus), 3, "You need to have at least 3 menus with name 'menu'")
