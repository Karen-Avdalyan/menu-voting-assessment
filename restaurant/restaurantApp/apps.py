from django.apps import AppConfig


class RestaurantappConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "restaurant.restaurantApp"

    def ready(self):
        print("ready")