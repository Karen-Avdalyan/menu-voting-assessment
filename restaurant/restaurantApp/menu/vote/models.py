from django.db import models

SCORE_CHOICES = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
)


class Vote(models.Model):
    score = models.CharField(
        max_length=20,
        choices=SCORE_CHOICES
    )
    user = models.ForeignKey(
        "restaurantApp.Employee",
        related_name="votes",
        on_delete=models.CASCADE,
    )
    menu = models.ForeignKey(
        "restaurantApp.Menu",
        related_name="votes",
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = 'votes'
        app_label = 'restaurantApp'
