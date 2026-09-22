from .events import OrderCreated


class OrderCreatedHandler:
    def __init__(self) -> None:
        self.handled_events: list[OrderCreated] = []

    def handle(
        self,
        event: OrderCreated,
    ) -> None:
        self.handled_events.append(event)

        print(f"Evento manejado: OrderCreated para order {event.order_id}")
