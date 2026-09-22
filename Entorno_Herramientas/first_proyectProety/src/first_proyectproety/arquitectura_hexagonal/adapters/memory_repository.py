from ..domain.order import Order


class MemoryOrderRepository:
    def __init__(self) -> None:
        self._orders: dict[int, Order] = {}

    def save(
        self,
        order: Order,
    ) -> None:
        self._orders[order.id] = order

    def get(
        self,
        order_id: int,
    ) -> Order | None:
        return self._orders.get(order_id)
