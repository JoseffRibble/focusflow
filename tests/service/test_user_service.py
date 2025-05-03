from unittest.mock import Mock

import pytest

from core.services.user_service import UserService


@pytest.fixture
def mock_repo():
    return Mock()


@pytest.fixture
def service(mock_repo):
    return UserService(mock_repo)


@pytest.mark.django_db
class TestUserRegistration:
    def test_register_user_success(self, service, mock_repo):
        mock_repo.exists_by_email.return_value = False
        mock_repo.save.return_value = {"email": "test@example.com"}
        result = service.register_user("user1", "test@example.com", "strongpwd")
        assert result["email"] == "test@example.com"
        mock_repo.save.assert_called_once()

    def test_register_user_email_exists(self, service, mock_repo):
        mock_repo.exists_by_email.return_value = True
        with pytest.raises(ValueError, match="Email already registered"):
            service.register_user("user1", "test@example.com", "strongpwd")

    def test_register_user_invalid_password(self, service, mock_repo):
        mock_repo.exists_by_email.return_value = False
        with pytest.raises(ValueError, match="Invalid password"):
            service.register_user("user1", "test@example.com", "123")


@pytest.mark.django_db
class TestUserLogin:
    def test_login_user_success(self, service, mock_repo):
        user_mock = Mock()
        user_mock.check_password.return_value = True
        mock_repo.find_by_email.return_value = user_mock
        result = service.login_user("test@example.com", "validpwd")
        assert result == user_mock

    def test_login_user_invalid(self, service, mock_repo):
        mock_repo.find_by_email.return_value = None
        with pytest.raises(ValueError, match="Invalid credentials"):
            service.login_user("notfound@example.com", "any")


@pytest.mark.django_db
class TestUserRoleAssignment:
    def test_assign_role_success(self, service, mock_repo):
        user_mock = Mock()
        mock_repo.find_by_id.return_value = user_mock
        result = service.assign_role(1, "admin")
        assert user_mock.role == "admin"
        mock_repo.update.assert_called_once_with(user_mock)

    def test_assign_role_user_not_found(self, service, mock_repo):
        mock_repo.find_by_id.return_value = None
        with pytest.raises(ValueError, match="User not found"):
            service.assign_role(999, "admin")


@pytest.mark.django_db
class TestTeamMembership:
    def test_add_user_to_team_success(self, service, mock_repo):
        user_mock = Mock()
        user_mock.teams = set()
        mock_repo.find_by_id.return_value = user_mock
        result = service.add_user_to_team(1, 101)
        assert 101 in user_mock.teams
        mock_repo.update.assert_called_once_with(user_mock)

    def test_add_user_to_team_user_not_found(self, service, mock_repo):
        mock_repo.find_by_id.return_value = None
        with pytest.raises(ValueError, match="User not found"):
            service.add_user_to_team(1, 101)

    def test_remove_user_from_team_success(self, service, mock_repo):
        user_mock = Mock()
        user_mock.teams = {101, 102}
        mock_repo.find_by_id.return_value = user_mock
        result = service.remove_user_from_team(1, 101)
        assert 101 not in user_mock.teams
        mock_repo.update.assert_called_once_with(user_mock)

    def test_remove_user_from_team_user_not_found(self, service, mock_repo):
        mock_repo.find_by_id.return_value = None
        with pytest.raises(ValueError, match="User not found"):
            service.remove_user_from_team(1, 101)
