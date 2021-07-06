from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Post

class WallTests(APITestCase):
    def test_post_noutification_woll(self):
        response = self.client.get('/api/v1/wall/1')
        print(response)
