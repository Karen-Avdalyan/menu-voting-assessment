from django.core.management.base import BaseCommand

from restaurant.restaurantApp.utils.seed_test_db import SeedTestDB


class Command(BaseCommand):
    help = 'Initialize db with data'

    def handle(self, *args, **kwargs):
        SeedTestDB.createGroups()
        SeedTestDB.createTestAdmin()
