from django.db import models

from restaurant.restaurantApp.user.restaurant_manager.models import RestaurantWorker


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    manager = models.ForeignKey(
        to=RestaurantWorker,
        related_name='restaurants',
        on_delete=models.PROTECT
    )

    class Meta:
        db_table = 'restaurants'
        app_label = 'restaurantApp'
        ordering = ['-id']
