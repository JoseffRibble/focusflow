import pytest
from core.models import User
from django.urls import reverse
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_register_user_success():
    client = APIClient()
    data = {"username": "newuser", "email": "new@example.com", "password": "secure123"}
    response = client.post(reverse("register"), data)
    assert response.status_code == 201
    assert User.objects.filter(email="new@example.com").exists()
