import pytest
from django.utils import timezone

from core.models import Task, TaskPriority, User
from core.models.enums import TaskStatus


@pytest.mark.django_db
class TestTaskStatus:
    def setup_method(self):
        self.user = User.objects.create_user(
            username="flowuser", email="f@f.com", password="pass"
        )
        self.task = Task.objects.create(
            title="Status Flow",
            short_description="sd",
            long_description="ld",
            due_date=timezone.now().date(),
            priority=TaskPriority.MEDIUM,
            assignee_user=self.user,
        )

    def test_valid_status_update(self):
        self.task.update_status(TaskStatus.PENDING)
        assert self.task.status == TaskStatus.PENDING

        self.task.update_status(TaskStatus.IN_REVIEW)
        assert self.task.status == TaskStatus.IN_REVIEW

        self.task.update_status(TaskStatus.CLOSED)
        assert self.task.status == TaskStatus.CLOSED

    def test_invalid_status_rejected(self):
        prev = self.task.status
        self.task.update_status("INVALID_STATUS")
        assert self.task.status == prev
