from __future__ import annotations

from django.db import models

from core.models.user import User


class Team(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    members = models.ManyToManyField(User, related_name="teams")

    def add_member(self, user: User) -> None:
        self.members.add(user)

    def remove_member(self, user: User) -> None:
        self.members.remove(user)

    class Meta:
        verbose_name = "Team"
        verbose_name_plural = "Teams"
        ordering = ["name"]
