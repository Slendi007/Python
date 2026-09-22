from ..domain.order import Order
from .ports import (
    OrderNotifier,
    OrderRepository,
)


class CreateOrder:
    def __init__(
        self,
        repository: OrderRepository,
        notifier: OrderNotifier,
    ) -> None:
        self.repository = repository
        self.notifier = notifier

    def execute(
        self,
        order_id: int,
        customer: str,
        product: str,
        quantity: int,
    ) -> Order:
        if quantity <= 0:
            raise ValueError("La cantidad debe ser mayor que cero")

        order = Order(
            id=order_id,
            customer=customer,
            product=product,
            quantity=quantity,
        )

        self.repository.save(order)

        self.notifier.notify_created(order)

        return order
