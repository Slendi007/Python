from ..application.ports import OrderRepository
from ..entities.order import Order


class MemoryOrderRepository:
    def __init__(self) -> None:
        self._orders: dict[int, Order] = {}

    def add(
        self,
        order: Order,
    ) -> None:
        self._orders[order.id] = order

    def get(
        self,
        order_id: int,
    ) -> Order | None:
        return self._orders.get(order_id)


class MemoryUnitOfWork:
    def __init__(self) -> None:
        self.orders: OrderRepository = MemoryOrderRepository()

        self.committed = False
        self.rolled_back = False

    def commit(self) -> None:
        self.committed = True

    def rollback(self) -> None:
        self.rolled_back = True
