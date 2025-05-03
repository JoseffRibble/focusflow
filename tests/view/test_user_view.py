import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from core.models import User


@pytest.mark.django_db
def test_register_user_success():
    client = APIClient()
    data = {"username": "newuser", "email": "new@example.com", "password": "secure123"}
    response = client.post(reverse("register"), data)
    assert response.status_code == 201
    assert User.objects.filter(email="new@example.com").exists()
