from sqlalchemy import select
from sqlalchemy.orm import Session

from .models import Order
from .schemas import OrderCreate, OrderUpdate


def crear_order(
    session: Session,
    datos: OrderCreate,
) -> Order:
    order = Order(
        customer=datos.customer,
        product=datos.product,
        quantity=datos.quantity,
        price=datos.price,
    )

    session.add(order)
    session.commit()
    session.refresh(order)

    return order


def obtener_orders(
    session: Session,
) -> list[Order]:
    consulta = select(Order)

    return list(session.scalars(consulta))


def obtener_order(
    session: Session,
    order_id: int,
) -> Order | None:
    return session.get(
        Order,
        order_id,
    )


def actualizar_order(
    session: Session,
    order_id: int,
    datos: OrderUpdate,
) -> Order | None:
    order = session.get(
        Order,
        order_id,
    )

    if order is None:
        return None

    order.customer = datos.customer
    order.product = datos.product
    order.quantity = datos.quantity
    order.price = datos.price

    session.commit()
    session.refresh(order)

    return order


def eliminar_order(
    session: Session,
    order_id: int,
) -> bool:
    order = session.get(
        Order,
        order_id,
    )

    if order is None:
        return False

    session.delete(order)
    session.commit()

    return True
