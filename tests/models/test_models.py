from datetime import timedelta

import pytest
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils import timezone

from core.models import Task, Team, User
from core.models.enums import TaskPriority


@pytest.mark.django_db
class TestUserModel:
    def test_create_user_valid(self):
        user = User.objects.create_user(
            username="user1", email="user@example.com", password="Valid123!"
        )
        assert user.email == "user@example.com"

    def test_create_user_invalid_email(self):
        with pytest.raises(ValidationError):
            validate_email("invalid")

    def test_create_user_short_password(self):
        with pytest.raises(ValueError):
            User.objects.create_user(
                username="shortpwd", email="short@ex.com", password="12345"
            )

    def test_create_user_empty_password(self):
        with pytest.raises(ValueError):
            User.objects.create_user(
                username="emptypwd", email="empty@ex.com", password=""
            )


@pytest.mark.django_db
class TestTeamModel:
    def test_create_team_valid(self):
        team = Team.objects.create(name="Alpha", description="desc")
        assert team.name == "Alpha"

    def test_create_team_with_empty_name(self):
        team = Team.objects.create(name="", description="desc")
        assert team.name == ""

    def test_add_member_to_team(self):
        team = Team.objects.create(name="TeamX", description="test")
        user = User.objects.create_user(
            username="user", email="u@e.com", password="pass123"
        )
        team.add_member(user)
        assert user in team.members.all()


@pytest.mark.django_db
class TestTaskModel:
    def test_create_task_valid(self):
        task = Task.objects.create(
            title="Fix Bug",
            short_description="short",
            long_description="long",
            due_date=timezone.now().date() + timedelta(days=3),
            priority=TaskPriority.HIGH,
        )
        assert task.title == "Fix Bug"

    def test_create_task_without_due_date(self):
        with pytest.raises(Exception):  # due_date is NOT NULL
            Task.objects.create(
                title="No Due Date",
                short_description="short",
                long_description="long",
                priority=TaskPriority.MEDIUM,
            )

    def test_create_task_with_empty_title(self):
        task = Task.objects.create(
            title="",
            short_description="short",
            long_description="long",
            due_date=timezone.now().date(),
            priority=TaskPriority.HIGH,
        )
        assert task.title == ""

    def test_assign_task_to_user(self):
        task = Task.objects.create(
            title="Assign to User",
            short_description="short",
            long_description="long",
            due_date=timezone.now().date(),
            priority=TaskPriority.MEDIUM,
        )
        user = User.objects.create_user(
            username="assignee", email="a@a.com", password="123456"
        )
        task.assign_to_user(user)
        assert task.assignee_user == user
        assert task.assignee_team is None

    def test_assign_task_to_team(self):
        task = Task.objects.create(
            title="Assign to Team",
            short_description="short",
            long_description="long",
            due_date=timezone.now().date(),
            priority=TaskPriority.LOW,
        )
        team = Team.objects.create(name="Bravo", description="desc")
        task.assign_to_team(team)
        assert task.assignee_team == team
        assert task.assignee_user is None

    def test_assign_task_to_nonexistent_user(self):
        task = Task.objects.create(
            title="Invalid Assignment",
            short_description="s",
            long_description="l",
            due_date=timezone.now().date(),
            priority=TaskPriority.LOW,
        )
        with pytest.raises(User.DoesNotExist):
            user = User.objects.get(pk=9999)
            task.assign_to_user(user)

    # Decision Table Logic Test – Task assignment mutual exclusion
    def test_task_initial_state_unassigned(self):
        task = Task.objects.create(
            title="Unassigned Task",
            short_description="s",
            long_description="l",
            due_date=timezone.now().date(),
            priority=TaskPriority.LOW,
        )
        assert task.assignee_user is None
        assert task.assignee_team is None

    def test_task_assign_user_then_team(self):
        task = Task.objects.create(
            title="Switch Assignment",
            short_description="s",
            long_description="l",
            due_date=timezone.now().date(),
            priority=TaskPriority.LOW,
        )
        user = User.objects.create_user(
            username="u", email="u@u.com", password="pass123"
        )
        team = Team.objects.create(name="TeamA", description="test")
        task.assign_to_user(user)
        assert task.assignee_user == user
        assert task.assignee_team is None

        task.assign_to_team(team)
        assert task.assignee_team == team
        assert task.assignee_user is None
