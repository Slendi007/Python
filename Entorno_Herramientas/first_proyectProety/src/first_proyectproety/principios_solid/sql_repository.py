from sqlalchemy import Integer, String, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column

from .models import User


class Base(DeclarativeBase):
    pass


class UserTable(Base):
    __tablename__ = "solid_users"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    name: Mapped[str] = mapped_column(
        String(100),
    )

    email: Mapped[str] = mapped_column(
        String(150),
    )


class SQLUserRepository:
    def __init__(
        self,
        session: Session,
    ) -> None:
        self.session = session

    def add(self, user: User) -> None:
        row = UserTable(
            id=user.id,
            name=user.name,
            email=user.email,
        )

        self.session.add(row)
        self.session.commit()

    def get(
        self,
        user_id: int,
    ) -> User | None:
        row = self.session.get(
            UserTable,
            user_id,
        )

        if row is None:
            return None

        return User(
            id=row.id,
            name=row.name,
            email=row.email,
        )

    def get_all(self) -> list[User]:
        rows = self.session.scalars(select(UserTable))

        return [
            User(
                id=row.id,
                name=row.name,
                email=row.email,
            )
            for row in rows
        ]

    def delete(
        self,
        user_id: int,
    ) -> bool:
        row = self.session.get(
            UserTable,
            user_id,
        )

        if row is None:
            return False

        self.session.delete(row)
        self.session.commit()

        return True
