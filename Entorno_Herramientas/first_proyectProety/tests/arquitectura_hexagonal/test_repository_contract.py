from collections.abc import Iterator

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from first_proyectproety.arquitectura_hexagonal.adapters.memory_repository import (
    MemoryOrderRepository,
)
from first_proyectproety.arquitectura_hexagonal.adapters.sqlalchemy_repository import (
    Base,
    SQLAlchemyOrderRepository,
)
from first_proyectproety.arquitectura_hexagonal.application.ports import (
    OrderRepository,
)
from first_proyectproety.arquitectura_hexagonal.domain.order import (
    Order,
)


@pytest.fixture(
    params=[
        "memory",
        "sqlalchemy",
    ]
)
def repository(
    request: pytest.FixtureRequest,
) -> Iterator[OrderRepository]:
    if request.param == "memory":
        yield MemoryOrderRepository()
        return

    engine = create_engine(
        "sqlite://",
    )

    Base.metadata.create_all(engine)

    with Session(engine) as session:
        yield SQLAlchemyOrderRepository(session)

    Base.metadata.drop_all(engine)


def test_repository_save_and_get(
    repository: OrderRepository,
) -> None:
    order = Order(
        id=1,
        customer="Cesar",
        product="Laptop",
        quantity=2,
    )

    repository.save(order)

    resultado = repository.get(1)

    assert resultado == order


def test_repository_returns_none_when_missing(
    repository: OrderRepository,
) -> None:
    resultado = repository.get(999)

    assert resultado is None
