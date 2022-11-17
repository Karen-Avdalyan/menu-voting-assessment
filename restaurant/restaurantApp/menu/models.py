from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    restaurant = models.ForeignKey(
        "restaurantApp.Restaurant",
        related_name="menus",
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = 'menus'
        app_label = 'restaurantApp'
        ordering = ['-id']
