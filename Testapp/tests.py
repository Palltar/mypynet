from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from src.profiles.models import UserNet

class AccountTests(APITestCase):
    def test_create_account(self):
        url = reverse('account-list')
        data = {'name': 'DabApps'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(UserNet.objects.count(), 1)
        self.assertEqual(UserNet.objects.get().name, 'DabApps')


