from sqlalchemy import Float, String
from sqlalchemy.orm import Mapped, mapped_column

from .database import Base


class Order(Base):
    __tablename__ = "fastapi_orders"

    id: Mapped[int] = mapped_column(
        primary_key=True,
    )

    customer: Mapped[str] = mapped_column(
        String(100),
    )

    product: Mapped[str] = mapped_column(
        String(100),
    )

    quantity: Mapped[int]

    price: Mapped[float] = mapped_column(
        Float,
    )
