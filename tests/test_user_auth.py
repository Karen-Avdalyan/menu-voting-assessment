from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from restaurant.restaurantApp.utils.seed_test_db import SeedTestDB


class TestUserViews(APITestCase):
    @classmethod
    def setUpTestData(cls):
        SeedTestDB.createAll()

    def test_access_token(self):
        admin_user = User.objects.get(username="adm")

        token_obtain_url = reverse('token_obtain_pair')
        client = APIClient()

        resp = client.post(token_obtain_url, {'username': 'adm', 'password': 'adm'}, format='json')
        assert 'access' in resp.data
        token = resp.data['access']
        client.force_authenticate(admin_user, token)

        verify_url = reverse('user-employee')
        resp = client.get(verify_url, data={'format': 'json'})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        return client

    def test_restaurant_worker_token(self):
        restaurant_worker = User.objects.get(username="restaurant_worker")

        token_obtain_url = reverse('token_obtain_pair')
        client = APIClient()

        resp = client.post(token_obtain_url, {'username': restaurant_worker.username, 'password': '12345678'}, format='json')
        assert 'access' in resp.data
        token = resp.data['access']
        client.force_authenticate(restaurant_worker, token)

        verify_url = reverse('user-employee')
        resp = client.get(verify_url, data={'format': 'json'})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        return client

    def test_employee_token(self):
        employee = User.objects.get(username="employee")

        token_obtain_url = reverse('token_obtain_pair')
        client = APIClient()

        resp = client.post(token_obtain_url, {'username': employee.username, 'password': '12345678'}, format='json')
        assert 'access' in resp.data
        token = resp.data['access']
        client.force_authenticate(employee, token)

        verify_url = reverse('user-employee')
        resp = client.get(verify_url, data={'format': 'json'})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        return client

    def test_old_employee_token(self):
        restaurant_worker = User.objects.get(username="employee")

        token_obtain_url = reverse('token_obtain_pair')
        client = APIClient(**{"Build-Version": '1.0.0'})

        resp = client.post(token_obtain_url, {'username': restaurant_worker.username, 'password': '12345678'},
                           format='json')
        assert 'access' in resp.data
        token = resp.data['access']
        client.force_authenticate(restaurant_worker, token)

        verify_url = reverse('user-employee')
        resp = client.get(verify_url, data={'format': 'json'})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        return client
