import pytest

from first_proyectproety.arquitectura_hexagonal.adapters.http_notifier import (
    HTTPOrderNotifier,
)
from first_proyectproety.arquitectura_hexagonal.adapters.memory_repository import (
    MemoryOrderRepository,
)
from first_proyectproety.arquitectura_hexagonal.application.create_order import (
    CreateOrder,
)


def test_create_order() -> None:
    repository = MemoryOrderRepository()
    notifier = HTTPOrderNotifier()

    use_case = CreateOrder(
        repository,
        notifier,
    )

    order = use_case.execute(
        order_id=1,
        customer="Cesar",
        product="Laptop",
        quantity=2,
    )

    assert order.id == 1
    assert order.product == "Laptop"

    saved = repository.get(1)

    assert saved == order

    assert len(notifier.sent_notifications) == 1


def test_create_order_quantity_invalid() -> None:
    repository = MemoryOrderRepository()
    notifier = HTTPOrderNotifier()

    use_case = CreateOrder(
        repository,
        notifier,
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
