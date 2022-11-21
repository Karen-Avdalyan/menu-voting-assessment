from django.core.management.base import BaseCommand

from restaurant.restaurantApp.utils.seed_test_db import SeedTestDB


class Command(BaseCommand):
    help = 'Initialize test db with test data'

    def handle(self, *args, **kwargs):
        SeedTestDB.createAll()
