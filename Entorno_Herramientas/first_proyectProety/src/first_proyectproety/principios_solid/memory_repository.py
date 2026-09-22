from .models import User


class MemoryUserRepository:
    def __init__(self) -> None:
        self._users: dict[int, User] = {}

    def add(self, user: User) -> None:
        self._users[user.id] = user

    def get(self, user_id: int) -> User | None:
        return self._users.get(user_id)

    def get_all(self) -> list[User]:
        return list(self._users.values())

    def delete(self, user_id: int) -> bool:
        if user_id not in self._users:
            return False

        del self._users[user_id]
        return True
