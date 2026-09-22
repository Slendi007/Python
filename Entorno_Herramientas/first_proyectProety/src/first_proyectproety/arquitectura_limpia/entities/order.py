from dataclasses import dataclass


@dataclass
class Order:
    id: int
    customer: str
    product: str
    quantity: int
