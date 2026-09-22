from __future__ import annotations

from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        primary_key=True,
    )

    name: Mapped[str] = mapped_column(
        String(100),
    )

    email: Mapped[str] = mapped_column(
        String(150),
        unique=True,
    )

    orders: Mapped[list[Order]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan",
    )


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(
        primary_key=True,
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
    )

    user: Mapped[User] = relationship(
        back_populates="orders",
    )

    items: Mapped[list[OrderItem]] = relationship(
        back_populates="order",
        cascade="all, delete-orphan",
    )


class OrderItem(Base):
    __tablename__ = "order_items"

    id: Mapped[int] = mapped_column(
        primary_key=True,
    )

    order_id: Mapped[int] = mapped_column(
        ForeignKey("orders.id"),
    )

    product: Mapped[str] = mapped_column(
        String(100),
    )

    quantity: Mapped[int]

    price: Mapped[float]

    order: Mapped[Order] = relationship(
        back_populates="items",
    )
