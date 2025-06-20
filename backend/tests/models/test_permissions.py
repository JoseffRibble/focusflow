import pytest
from core.models import Task, TaskPriority, User
from django.utils import timezone


@pytest.mark.django_db
class TestTaskPermissions:
    def test_only_assignee_can_edit(self):
        user1 = User.objects.create_user(
            username="user1", email="assignee@example.com", password="pass123"
        )
        user2 = User.objects.create_user(
            username="user2", email="other@example.com", password="pass123"
        )
        task = Task.objects.create(
            title="Secure",
            short_description="s",
            long_description="l",
            due_date=timezone.now().date(),
            priority=TaskPriority.LOW,
            assignee_user=user1,
        )
        assert task.can_user_edit(user1)
        assert not task.can_user_edit(user2)
