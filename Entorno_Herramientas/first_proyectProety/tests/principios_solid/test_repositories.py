from collections.abc import Iterator

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from first_proyectproety.principios_solid.memory_repository import (
    MemoryUserRepository,
)
from first_proyectproety.principios_solid.models import User
from first_proyectproety.principios_solid.ports import UserRepository
from first_proyectproety.principios_solid.sql_repository import (
    Base,
    SQLUserRepository,
)


@pytest.fixture(
    params=[
        "memory",
        "sql",
    ]
)
def repository(
    request: pytest.FixtureRequest,
) -> Iterator[UserRepository]:

    if request.param == "memory":
        yield MemoryUserRepository()
        return

    engine = create_engine(
        "sqlite://",
    )

    Base.metadata.create_all(engine)

    with Session(engine) as session:
        yield SQLUserRepository(session)


def test_add_y_get(
    repository: UserRepository,
) -> None:
    user = User(
        id=1,
        name="Cesar",
        email="cesar@example.com",
    )

    repository.add(user)

    resultado = repository.get(1)

    assert resultado == user


def test_get_all(
    repository: UserRepository,
) -> None:
    repository.add(
        User(
            id=1,
            name="Cesar",
            email="cesar@example.com",
        )
    )

    repository.add(
        User(
            id=2,
            name="Ana",
            email="ana@example.com",
        )
    )

    usuarios = repository.get_all()

    assert len(usuarios) == 2


def test_delete(
    repository: UserRepository,
) -> None:
    user = User(
        id=1,
        name="Cesar",
        email="cesar@example.com",
    )

    repository.add(user)

    eliminado = repository.delete(1)

    assert eliminado is True

    assert repository.get(1) is None


def test_delete_usuario_inexistente(
    repository: UserRepository,
) -> None:
    eliminado = repository.delete(999)

    assert eliminado is False
