from ..entities.order import Order
from .event_handlers import (
    OrderCreatedHandler,
)
from .events import OrderCreated
from .ports import UnitOfWork


class CreateOrder:
    def __init__(
        self,
        uow: UnitOfWork,
        event_handler: OrderCreatedHandler,
    ) -> None:
        self.uow = uow
        self.event_handler = event_handler

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

        try:
            self.uow.orders.add(order)

            self.uow.commit()

        except Exception:
            self.uow.rollback()

            raise

        event = OrderCreated(
            order_id=order.id,
            customer=order.customer,
        )

        self.event_handler.handle(event)

        return order
