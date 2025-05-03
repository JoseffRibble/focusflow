from __future__ import annotations

from typing import Any, Optional

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager["User"]):
    def create_user(
        self,
        username: str,
        email: Optional[str] = None,
        password: Optional[str] = None,
        **extra_fields: Any,
    ) -> User:
        if not password:
            raise ValueError("Password must not be empty.")
        if len(password) < 6:
            raise ValueError("Password must be at least 6 characters long.")
        if not email:
            raise ValueError("Email must be set.")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self,
        username: str,
        email: Optional[str] = None,
        password: Optional[str] = None,
        **extra_fields: Any,
    ) -> User:
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    email: str = models.EmailField(unique=True)
    first_name: str = models.CharField(max_length=150)
    last_name: str = models.CharField(max_length=150)
    role: str = models.CharField(max_length=20, default="member")

    created_at: Any = models.DateTimeField(auto_now_add=True)
    last_login: Any = models.DateTimeField(null=True, blank=True)

    groups = models.ManyToManyField(
        "auth.Group", related_name="focusflow_users", blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission", related_name="focusflow_user_permissions", blank=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = UserManager()

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["-created_at"]
