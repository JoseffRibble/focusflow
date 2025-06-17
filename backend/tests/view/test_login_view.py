from core.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class LoginViewTests(APITestCase):
    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(
            username="testuser", email="t@t.com", password="testpass123"
        )
        self.login_url = reverse("login")

    def test_login_success(self):
        response = self.client.post(
            self.login_url,
            {"email": "t@t.com", "password": "testpass123"},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)

    def test_login_fail_invalid_password(self):
        response = self.client.post(
            self.login_url,
            {"email": "t@t.com", "password": "wrongpass"},
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn("detail", response.data)
