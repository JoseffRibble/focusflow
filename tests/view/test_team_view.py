import pytest
from rest_framework.test import APIClient

from core.models import Team


@pytest.mark.django_db
def test_create_team_success():
    client = APIClient()
    data = {"name": "Dev Team", "description": "Backend team"}
    response = client.post("/api/teams/", data)
    assert response.status_code == 201
    assert Team.objects.filter(name="Dev Team").exists()
