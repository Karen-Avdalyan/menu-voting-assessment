import datetime

from django.contrib.auth.models import User, Group
from rest_framework.test import APITestCase

from restaurant.restaurantApp.menu.menu_item.models import MenuItem
from restaurant.restaurantApp.menu.models import Menu
from restaurant.restaurantApp.restaurant.models import Restaurant
from restaurant.restaurantApp.user.employee.models import Employee
from restaurant.restaurantApp.user.restaurant_manager.models import RestaurantWorker
from restaurant.test_entities import TEST_ENTITIES


class TestSetup(APITestCase):
    def createAll(self):
        self.createTestAdmin()
        self.createGroups()
        self.createEmployee()
        self.createRestaurantWorker()
        self.createRestaurant()
        self.createMenus()

    def createTestAdmin(self):
        if not User.objects.filter(username=TEST_ENTITIES["users"]["admin"]["username"]):
            User.objects.create_superuser(
                username=TEST_ENTITIES["users"]["admin"]["username"],
                password=TEST_ENTITIES["users"]["admin"]["password"]
            )

    def createGroups(self):
        for group in TEST_ENTITIES["groups"]:
            Group.objects.get_or_create(name=group["name"])

    def createEmployee(self):
        if not Employee.objects.filter(username=TEST_ENTITIES["users"]["employee"]["username"]):
            user = Employee.objects.create(
                username=TEST_ENTITIES["users"]["employee"]["username"],
                password=TEST_ENTITIES["users"]["employee"]["password"],
            )
            employee_group = Group.objects.get(name="employee")
            employee_group.user_set.add(user)
            user.save()
            employee_group.save()

    def createRestaurantWorker(self):
        if not RestaurantWorker.objects.filter(username=TEST_ENTITIES["users"]["restaurant_worker"]["username"]):
            user, _ = User.objects.get_or_create(
                username=TEST_ENTITIES["users"]["restaurant_worker"]["username"],
                password=TEST_ENTITIES["users"]["restaurant_worker"]["password"],
            )
            restaurant_group = Group.objects.get(name="restaurant")
            restaurant_group.user_set.add(user)
            user.save()
            restaurant_group.save()
            return user
        return RestaurantWorker.objects.filter(username=TEST_ENTITIES["users"]["restaurant_worker"]["username"]).first()

    def createRestaurant(self):
        manager = self.createRestaurantWorker()
        restaurant, _ = Restaurant.objects.get_or_create(
            name=TEST_ENTITIES["restaurant"]["name"],
            manager=manager
        )
        return restaurant

    def createMenus(self):
        restaurant = self.createRestaurant()
        for menu_item in TEST_ENTITIES["menu"]["items"]:
            menu = Menu.objects.create(
                name=TEST_ENTITIES["menu"]["name"],
                date=datetime.date.today(),
                restaurant=restaurant,
            )
            MenuItem.objects.create(**menu_item, menu=menu)
