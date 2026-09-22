from dataclasses import dataclass


@dataclass
class OrderCreated:
    order_id: int
    customer: str
