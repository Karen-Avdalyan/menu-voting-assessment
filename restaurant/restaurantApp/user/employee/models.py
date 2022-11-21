import datetime

from django.contrib.auth.models import User, UserManager, Group
from django.db import models


class EmployeeManager(UserManager):
    def get_queryset(self):
        return super(EmployeeManager, self).get_queryset().filter(groups__name__in=["employee"])


class Employee(User):
    last_voted = models.DateField(default=datetime.date.min, null=True)
    objects = EmployeeManager()

    class Meta:
        db_table = 'auth_user_employee'
        app_label = 'restaurantApp'
        default_related_name = 'employee'
        ordering = ['-id']
