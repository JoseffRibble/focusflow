from typing import Any, Optional

from django.db.models import QuerySet

from core.models import User


class UserRepository:
    def create(self, **kwargs: Any) -> User:
        return User.objects.create(**kwargs)

    def find_by_id(self, user_id: int) -> Optional[User]:
        return User.objects.filter(id=user_id).first()

    def find_by_email(self, email: str) -> Optional[User]:
        return User.objects.filter(email=email).first()

    def update(self, user: User) -> User:
        user.save()
        return user

    def delete(self, user: User) -> None:
        user.delete()

    def find_by_role(self, role: str) -> QuerySet[User]:
        return User.objects.filter(role=role)

    def find_by_team(self, team_id: int) -> QuerySet[User]:
        return User.objects.filter(teams__id=team_id).distinct()
