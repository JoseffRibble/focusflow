from django.db import models


class TaskPriority(models.TextChoices):
    LOW = "LOW", "Low"
    MEDIUM = "MEDIUM", "Medium"
    HIGH = "HIGH", "High"


class TaskStatus(models.TextChoices):
    OPEN = "OPEN", "Open"
    PENDING = "PENDING", "Pending"
    IN_REVIEW = "IN_REVIEW", "In Review"
    CLOSED = "CLOSED", "Closed"
