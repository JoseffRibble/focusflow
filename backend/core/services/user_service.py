from typing import Any, Optional, Protocol


class UserRepositoryProtocol(Protocol):
    def exists_by_email(self, email: str) -> bool: ...
    def save(self, username: str, email: str, password: str) -> dict[str, Any]: ...
    def find_by_email(self, email: str) -> Optional[Any]: ...
    def find_by_id(self, user_id: int) -> Optional[Any]: ...
    def update(self, user: Any) -> None: ...


class UserService:
    def __init__(self, user_repo: UserRepositoryProtocol) -> None:
        self.user_repo = user_repo

    def register_user(self, username: str, email: str, password: str) -> dict[str, Any]:
        if self.user_repo.exists_by_email(email):
            raise ValueError("Email already registered")
        if not self._is_valid_password(password):
            raise ValueError("Invalid password")
        return self.user_repo.save(username, email, password)

    def login_user(self, email: str, password: str) -> Any:
        user = self.user_repo.find_by_email(email)
        if not user or not user.check_password(password):
            raise ValueError("Invalid credentials")
        return user

    def assign_role(self, user_id: int, role: str) -> Any:
        user = self.user_repo.find_by_id(user_id)
        if not user:
            raise ValueError("User not found")
        user.role = role
        self.user_repo.update(user)
        return user

    def add_user_to_team(self, user_id: int, team_id: int) -> Any:
        user = self.user_repo.find_by_id(user_id)
        if not user:
            raise ValueError("User not found")
        user.teams.add(team_id)
        self.user_repo.update(user)
        return user

    def remove_user_from_team(self, user_id: int, team_id: int) -> Any:
        user = self.user_repo.find_by_id(user_id)
        if not user:
            raise ValueError("User not found")
        user.teams.remove(team_id)
        self.user_repo.update(user)
        return user

    def _is_valid_password(self, password: Optional[str]) -> bool:
        return bool(password and len(password) >= 6)
