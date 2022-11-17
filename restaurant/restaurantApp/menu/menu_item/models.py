from django.db import models

from restaurant.restaurantApp.user.restaurant_manager.models import RestaurantWorker


class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=4095, default="")
    price = models.FloatField(blank=False, null=False)
    menu = models.ForeignKey(
        "restaurantApp.Menu",
        related_name="items",
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = 'menu_items'
        app_label = 'restaurantApp'
        ordering = ['-id']
