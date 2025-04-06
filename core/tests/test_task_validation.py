import pytest
from django.core.exceptions import ValidationError
from django.utils import timezone

from core.models import Task, User


@pytest.mark.django_db
class TestTaskValidation:
    def test_required_fields(self):
        task = Task()
        with pytest.raises(Exception):
            task.full_clean()

    def test_invalid_priority(self):
        user = User.objects.create_user(
            username="testuser", email="test@example.com", password="Test@1234"
        )
        task = Task(
            title="Bad",
            short_description="bad",
            long_description="bad",
            due_date=timezone.now().date(),
            priority="INVALID",
            assignee_user=user,
        )
        with pytest.raises(ValidationError):
            task.full_clean()
