import pytest
from core.models import Team, User
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken


@pytest.mark.django_db
def test_create_team_success():
    user = User.objects.create_user(
        username="testuser", email="test@example.com", password="testpass"
    )
    token = str(RefreshToken.for_user(user).access_token)

    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")

    data = {"name": "Dev Team", "description": "Backend team"}
    response = client.post("/api/teams/", data)
    assert response.status_code == 201
    assert Team.objects.filter(name="Dev Team").exists()
