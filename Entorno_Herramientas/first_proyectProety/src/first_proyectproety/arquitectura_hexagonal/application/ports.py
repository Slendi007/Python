from typing import Protocol

from ..domain.order import Order


class OrderRepository(Protocol):
    def save(
        self,
        order: Order,
    ) -> None: ...

    def get(
        self,
        order_id: int,
    ) -> Order | None: ...


class OrderNotifier(Protocol):
    def notify_created(
        self,
        order: Order,
    ) -> None: ...
