from django.contrib.auth.models import User, UserManager, Group


class RestaurantWorkerManager(UserManager):
    def get_queryset(self):
        return super(RestaurantWorkerManager, self).get_queryset().filter(groups__in=["2"])


class RestaurantWorker(User):
    objects = RestaurantWorkerManager()

    class Meta:
        proxy = True
        app_label = 'restaurantApp'
        ordering = ['-id']
