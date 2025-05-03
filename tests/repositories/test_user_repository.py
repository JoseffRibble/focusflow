import pytest

from core.models import Team, User
from core.repositories.user_repository import UserRepository


@pytest.mark.django_db
class TestUserRepository:

    def setup_method(self):
        self.repo = UserRepository()
        self.team = Team.objects.create(name="Alpha", description="Team A")
        self.user = self.repo.create(
            username="testuser",
            email="test@example.com",
            password="Valid123!",
            role="member",
        )
        self.user.teams.add(self.team)

    def test_find_by_id(self):
        found = self.repo.find_by_id(self.user.id)
        assert found == self.user

    def test_find_by_email(self):
        found = self.repo.find_by_email("test@example.com")
        assert found == self.user

    def test_update_user(self):
        self.user.username = "updateduser"
        self.repo.update(self.user)
        assert User.objects.get(id=self.user.id).username == "updateduser"

    def test_delete_user(self):
        self.repo.delete(self.user)
        assert User.objects.filter(id=self.user.id).count() == 0

    def test_find_by_role(self):
        results = self.repo.find_by_role("member")
        assert self.user in results

    def test_find_by_team(self):
        results = self.repo.find_by_team(self.team.id)
        assert self.user in results
