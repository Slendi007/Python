from sqlalchemy import Integer, String
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    Session,
    mapped_column,
)

from ..domain.order import Order


class Base(DeclarativeBase):
    pass


class OrderTable(Base):
    __tablename__ = "hexagonal_orders"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    customer: Mapped[str] = mapped_column(
        String(100),
    )

    product: Mapped[str] = mapped_column(
        String(100),
    )

    quantity: Mapped[int] = mapped_column(
        Integer,
    )


class SQLAlchemyOrderRepository:
    def __init__(
        self,
        session: Session,
    ) -> None:
        self.session = session

    def save(
        self,
        order: Order,
    ) -> None:
        row = OrderTable(
            id=order.id,
            customer=order.customer,
            product=order.product,
            quantity=order.quantity,
        )

        self.session.add(row)
        self.session.commit()

    def get(
        self,
        order_id: int,
    ) -> Order | None:
        row = self.session.get(
            OrderTable,
            order_id,
        )

        if row is None:
            return None

        return Order(
            id=row.id,
            customer=row.customer,
            product=row.product,
            quantity=row.quantity,
        )
