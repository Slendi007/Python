from dataclasses import dataclass

from pydantic import BaseModel, Field


@dataclass
class Order:
    id: int
    product: str
    quantity: int
    unit_price: float
    tax_rate: float = 0.16

    @property
    def subtotal(self) -> float:
        return self.quantity * self.unit_price

    @property
    def tax(self) -> float:
        return self.subtotal * self.tax_rate

    @property
    def total(self) -> float:
        return self.subtotal + self.tax

    def __lt__(self, other: "Order") -> bool:
        if not isinstance(other, Order):
            return NotImplemented

        return self.total < other.total

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Order):
            return NotImplemented

        return self.id == other.id


class OrderIn(BaseModel):
    id: int
    product: str = Field(min_length=1)
    quantity: int = Field(gt=0)
    unit_price: float = Field(gt=0)
    tax_rate: float = Field(default=0.16, ge=0, le=1)


class OrderOut(BaseModel):
    id: int
    product: str
    quantity: int
    unit_price: float
    subtotal: float
    tax: float
    total: float
