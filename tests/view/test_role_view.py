import pytest
from rest_framework.test import APIClient

from core.models import User


@pytest.mark.django_db
def test_update_user_role():
    user = User.objects.create_user(
        username="testuser", email="t@t.com", password="pass123"
    )
    client = APIClient()
    response = client.post(f"/api/users/{user.id}/role", {"role": "admin"})
    assert response.status_code == 200
    user.refresh_from_db()
    assert user.role == "admin"
