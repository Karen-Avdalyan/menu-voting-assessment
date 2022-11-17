from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APIClient


token_obtain_url = reverse('token_obtain_pair')
admin_user = User.objects.get(username="admin")


def authenticate_user(user, password):
    res_client = APIClient()
    resp = res_client.post(token_obtain_url, {'username': user.username, 'password': password}, format='json')
    assert 'access' in resp.data
    token = resp.data['access']
    res_client.force_authenticate(user, token)
    return res_client
