from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class CustomUserListTest(APITestCase):

    EMAIL = 'normal@user.com'

    @classmethod
    def setUpTestData(cls):
        User = get_user_model()
        cls.user = User.objects.create_user(email=cls.EMAIL, password='pwd')

    def test_basic_get_returns(self):
        url = reverse('users:api_user_list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data),1)
        self.assertEqual(response.data[0]['email'], self.EMAIL)
