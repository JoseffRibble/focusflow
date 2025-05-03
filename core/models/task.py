from __future__ import annotations

from typing import Any

from django.db import models
from django.db.models.query import QuerySet

from core.models.enums import TaskPriority, TaskStatus
from core.models.team import Team
from core.models.user import User


class TaskManager(models.Manager["Task"]):
    def filter_tasks(self, **kwargs: Any) -> QuerySet[Task]:
        return self.filter(**kwargs)


class Task(models.Model):
    title: str = models.CharField(max_length=255)
    short_description: str = models.CharField(max_length=255)
    long_description: str = models.TextField()
    due_date: Any = models.DateField()
    priority: str = models.CharField(max_length=10, choices=TaskPriority.choices)
    status: str = models.CharField(
        max_length=15, choices=TaskStatus.choices, default=TaskStatus.OPEN
    )

    assignee_user: models.ForeignKey = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="assigned_tasks",
    )
    assignee_team: models.ForeignKey = models.ForeignKey(
        Team,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="tasks",
    )

    tags: Any = models.JSONField(blank=True, null=True)

    objects = TaskManager()

    def assign_to_user(self, user: User) -> None:
        self.assignee_user = user
        self.assignee_team = None
        self.save()

    def assign_to_team(self, team: Team) -> None:
        self.assignee_team = team
        self.assignee_user = None
        self.save()

    def update_status(self, new_status: str) -> None:
        if new_status in TaskStatus.values:
            self.status = new_status
            self.save()

    def can_user_edit(self, user: User) -> bool:
        return self.assignee_user == user

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
        ordering = ["due_date", "priority"]
