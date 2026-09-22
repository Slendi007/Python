from .models import User
from .ports import UserRepository


class UserService:
    def __init__(
        self,
        repository: UserRepository,
    ) -> None:
        self.repository = repository

    def crear_usuario(
        self,
        user_id: int,
        name: str,
        email: str,
    ) -> User:
        user = User(
            id=user_id,
            name=name,
            email=email,
        )

        self.repository.add(user)

        return user

    def obtener_usuario(
        self,
        user_id: int,
    ) -> User | None:
        return self.repository.get(user_id)

    def obtener_usuarios(self) -> list[User]:
        return self.repository.get_all()

    def eliminar_usuario(
        self,
        user_id: int,
    ) -> bool:
        return self.repository.delete(user_id)
