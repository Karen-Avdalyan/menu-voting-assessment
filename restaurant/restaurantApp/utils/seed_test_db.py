import datetime

from django.contrib.auth.models import User, Group

from restaurant.restaurantApp.menu.menu_item.models import MenuItem
from restaurant.restaurantApp.menu.models import Menu
from restaurant.restaurantApp.restaurant.models import Restaurant
from restaurant.restaurantApp.user.employee.models import Employee
from restaurant.restaurantApp.user.restaurant_manager.models import RestaurantWorker
from restaurant.test_entities import TEST_ENTITIES


class SeedTestDB:
    @staticmethod
    def createAll():
        SeedTestDB.createTestAdmin()
        SeedTestDB.createGroups()
        SeedTestDB.createEmployee()
        SeedTestDB.createRestaurantWorker()
        SeedTestDB.createRestaurant()
        SeedTestDB.createMenus()

    @staticmethod
    def createTestAdmin():
        if not User.objects.filter(username=TEST_ENTITIES["users"]["admin"]["username"]):
            User.objects.create_superuser(
                username=TEST_ENTITIES["users"]["admin"]["username"],
                password=TEST_ENTITIES["users"]["admin"]["password"]
            )

    @staticmethod
    def createGroups():
        for group in TEST_ENTITIES["groups"]:
            Group.objects.get_or_create(name=group["name"])

    @staticmethod
    def createEmployee():
        if not Employee.objects.filter(username=TEST_ENTITIES["users"]["employee"]["username"]):
            user = Employee.objects.create(
                username=TEST_ENTITIES["users"]["employee"]["username"],
            )
            user.set_password(TEST_ENTITIES["users"]["employee"]["password"])
            employee_group = Group.objects.get(name="employee")
            employee_group.user_set.add(user)
            user.save()
            employee_group.save()

    @staticmethod
    def createRestaurantWorker():
        if not RestaurantWorker.objects.filter(username=TEST_ENTITIES["users"]["restaurant_worker"]["username"]):
            user = User.objects.create(
                username=TEST_ENTITIES["users"]["restaurant_worker"]["username"],
            )
            user.set_password(TEST_ENTITIES["users"]["restaurant_worker"]["password"])
            restaurant_group = Group.objects.get(name="restaurant")
            restaurant_group.user_set.add(user)
            user.save()
            restaurant_group.save()
            return user
        return RestaurantWorker.objects.filter(username=TEST_ENTITIES["users"]["restaurant_worker"]["username"]).first()

    @staticmethod
    def createRestaurant():
        manager = SeedTestDB.createRestaurantWorker()
        restaurant, _ = Restaurant.objects.get_or_create(
            name=TEST_ENTITIES["restaurant"]["name"],
            manager=manager
        )
        return restaurant

    @staticmethod
    def createMenus():
        restaurant = SeedTestDB.createRestaurant()
        for menu_item in TEST_ENTITIES["menu"]["items"]:
            menu = Menu.objects.create(
                name=TEST_ENTITIES["menu"]["name"],
                date=datetime.date.today(),
                restaurant=restaurant,
            )
            MenuItem.objects.create(**menu_item, menu=menu)
