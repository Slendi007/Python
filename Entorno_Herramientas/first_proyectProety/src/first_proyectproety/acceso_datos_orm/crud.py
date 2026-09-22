from sqlalchemy import select
from sqlalchemy.orm import Session

from .models import Order, OrderItem, User


def crear_usuario(
    session: Session,
    name: str,
    email: str,
) -> User:
    usuario = User(
        name=name,
        email=email,
    )

    session.add(usuario)
    session.commit()
    session.refresh(usuario)

    return usuario


def obtener_usuario(
    session: Session,
    user_id: int,
) -> User | None:
    return session.get(
        User,
        user_id,
    )


def obtener_usuarios(
    session: Session,
) -> list[User]:
    consulta = select(User)

    return list(session.scalars(consulta))


def actualizar_usuario(
    session: Session,
    user_id: int,
    name: str,
) -> User | None:
    usuario = session.get(
        User,
        user_id,
    )

    if usuario is None:
        return None

    usuario.name = name

    session.commit()
    session.refresh(usuario)

    return usuario


def eliminar_usuario(
    session: Session,
    user_id: int,
) -> bool:
    usuario = session.get(
        User,
        user_id,
    )

    if usuario is None:
        return False

    session.delete(usuario)
    session.commit()

    return True


def crear_orden(
    session: Session,
    user_id: int,
) -> Order:
    orden = Order(
        user_id=user_id,
    )

    session.add(orden)
    session.commit()
    session.refresh(orden)

    return orden


def obtener_orden(
    session: Session,
    order_id: int,
) -> Order | None:
    return session.get(
        Order,
        order_id,
    )


def agregar_item(
    session: Session,
    order_id: int,
    product: str,
    quantity: int,
    price: float,
) -> OrderItem:
    item = OrderItem(
        order_id=order_id,
        product=product,
        quantity=quantity,
        price=price,
    )

    session.add(item)
    session.commit()
    session.refresh(item)

    return item
