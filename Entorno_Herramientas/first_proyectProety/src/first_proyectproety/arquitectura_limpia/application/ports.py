from typing import Protocol

from ..entities.order import Order


class OrderRepository(Protocol):
    def add(
        self,
        order: Order,
    ) -> None: ...

    def get(
        self,
        order_id: int,
    ) -> Order | None: ...


class UnitOfWork(Protocol):
    orders: OrderRepository

    def commit(self) -> None: ...

    def rollback(self) -> None: ...
