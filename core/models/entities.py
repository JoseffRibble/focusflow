from django.contrib.auth.models import AbstractUser
from django.db import models

from .enums import TaskPriority, TaskStatus


class User(AbstractUser):
    # Basic fields
    # id: CharField is automatically created by Django
    email = models.EmailField(unique=True)
    # password: CharField is automatically created by Django
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True, blank=True)

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="focusflow_users",  # To avoid conflicts with Django's default groups
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="focusflow_user_permissions",  # To avoid conflicts with Django's default permissions
        blank=True,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["-created_at"]


class Team(models.Model):
    # Basic fields
    # id: CharField is automatically created by Django
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)

    # Relationships
    members = models.ManyToManyField(User, related_name="teams")

    def add_member(self, user):
        self.members.add(user)

    def remove_member(self, user):
        self.members.remove(user)

    class Meta:
        verbose_name = "Team"
        verbose_name_plural = "Teams"
        ordering = ["name"]  # Order by name ascending


class TaskManager(models.Manager):
    def filter_tasks(self, **kwargs):
        return self.filter(**kwargs)


class Task(models.Model):
    title = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255)
    long_description = models.TextField()
    due_date = models.DateField()
    priority = models.CharField(max_length=10, choices=TaskPriority.choices)
    status = models.CharField(
        max_length=15, choices=TaskStatus.choices, default=TaskStatus.OPEN
    )

    assignee_user = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="assigned_tasks",
    )
    assignee_team = models.ForeignKey(
        Team, null=True, blank=True, on_delete=models.SET_NULL, related_name="tasks"
    )
    tags = models.JSONField(blank=True, null=True)

    objects = TaskManager()

    def assign_to_user(self, user):
        self.assignee_user = user
        self.assignee_team = None
        self.save()

    def assign_to_team(self, team):
        self.assignee_team = team
        self.assignee_user = None
        self.save()

    def update_status(self, new_status):
        if new_status in TaskStatus.values:
            self.status = new_status
            self.save()

    def can_user_edit(self, user):
        return self.assignee_user == user

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
        ordering = ["due_date", "priority"]
