import pytest
from core.models import User
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken


@pytest.mark.django_db
def test_update_user_role():
    user = User.objects.create_user(
        username="testuser", email="t@t.com", password="pass123"
    )
    token = str(RefreshToken.for_user(user).access_token)

    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")

    response = client.post(f"/api/users/{user.id}/role", {"role": "admin"})
    assert response.status_code == 200
    user.refresh_from_db()
    assert user.role == "admin"
