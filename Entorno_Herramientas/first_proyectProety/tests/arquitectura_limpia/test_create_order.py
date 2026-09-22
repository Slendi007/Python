import pytest

from first_proyectproety.arquitectura_limpia.adapters.memory_uow import (
    MemoryUnitOfWork,
)
from first_proyectproety.arquitectura_limpia.adapters.presenter import (
    OrderPresenter,
)
from first_proyectproety.arquitectura_limpia.application.create_order import (
    CreateOrder,
)
from first_proyectproety.arquitectura_limpia.application.event_handlers import (
    OrderCreatedHandler,
)


def test_create_order() -> None:
    uow = MemoryUnitOfWork()

    handler = OrderCreatedHandler()

    use_case = CreateOrder(
        uow,
        handler,
    )

    order = use_case.execute(
        order_id=1,
        customer="Cesar",
        product="Laptop",
        quantity=2,
    )

    assert order.id == 1

    assert uow.committed is True

    assert len(handler.handled_events) == 1


def test_invalid_quantity() -> None:
    uow = MemoryUnitOfWork()

    handler = OrderCreatedHandler()

    use_case = CreateOrder(
        uow,
        handler,
    )

    with pytest.raises(
        ValueError,
        match="cantidad",
    ):
        use_case.execute(
            order_id=1,
            customer="Cesar",
            product="Laptop",
            quantity=0,
        )


def test_presenter() -> None:
    uow = MemoryUnitOfWork()
    handler = OrderCreatedHandler()

    use_case = CreateOrder(
        uow,
        handler,
    )

    order = use_case.execute(
        order_id=1,
        customer="Ana",
        product="Monitor",
        quantity=1,
    )

    resultado = OrderPresenter.present(order)

    assert resultado["id"] == 1
    assert resultado["cliente"] == "Ana"
    assert resultado["producto"] == "Monitor"
