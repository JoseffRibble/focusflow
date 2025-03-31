
from datetime import timedelta
import pytest
from django.utils import timezone
from core.models import Task, Team, User
from core.models.enums import TaskPriority

@pytest.mark.django_db
class TestModelCreation:
    def test_user_creation(self):
        user = User.objects.create_user(
            username="memberuser", email="member@example.com", password="Test@1234"
        )
        assert user.email == "member@example.com"

    def test_team_membership(self):
        team = Team.objects.create(name="Alpha", description="desc")
        user = User.objects.create_user(
            username="testuser", email="test@example.com", password="Test@1234"
        )
        team.add_member(user)
        assert user in team.members.all()

    def test_task_creation(self):
        task = Task.objects.create(
            title="Fix Bug",
            short_description="short",
            long_description="long",
            due_date=timezone.now().date() + timedelta(days=3),
            priority=TaskPriority.HIGH,
        )
        assert task.title == "Fix Bug"

    def test_assign_to_user(self):
        task = Task.objects.create(
            title="Assign",
            short_description="s",
            long_description="l",
            due_date=timezone.now().date(),
            priority=TaskPriority.MEDIUM,
        )
        user = User.objects.create_user(username="assignee", email="a@a.com", password="123")
        task.assign_to_user(user)
        assert task.assignee_user == user
        assert task.assignee_team is None

    def test_assign_to_team(self):
        task = Task.objects.create(
            title="Assign Team",
            short_description="s",
            long_description="l",
            due_date=timezone.now().date(),
            priority=TaskPriority.LOW,
        )
        team = Team.objects.create(name="Bravo", description="Team B")
        task.assign_to_team(team)
        assert task.assignee_team == team
        assert task.assignee_user is None
