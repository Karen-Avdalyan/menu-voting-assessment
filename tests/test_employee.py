from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory

from restaurant.restaurantApp.user.employee.views import ListCreateEmployeeAPIView
from tests.test_user_auth import TestUserViews


class TestEmployeeViews(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = ListCreateEmployeeAPIView.as_view()
        self.url = reverse("user-employee")

        self.client = TestUserViews().test_access_token()

    def test_employee_POST(self):
        post_url = reverse('user-employee')
        resp = self.client.post(post_url, data={
            "username": "employee3334",
            "password": "12345678",
            "first_name": "test",
            "last_name": "asdf"
        })
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

    def test_employee_GET(self):
        get_url = reverse('user-employee')
        resp = self.client.get(get_url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
