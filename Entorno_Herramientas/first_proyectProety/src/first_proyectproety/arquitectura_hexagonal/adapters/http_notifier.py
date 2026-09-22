from ..domain.order import Order


class HTTPOrderNotifier:
    def __init__(self) -> None:
        self.sent_notifications: list[dict[str, object]] = []

    def notify_created(
        self,
        order: Order,
    ) -> None:
        payload = {
            "event": "order_created",
            "order_id": order.id,
            "customer": order.customer,
        }

        self.sent_notifications.append(payload)
