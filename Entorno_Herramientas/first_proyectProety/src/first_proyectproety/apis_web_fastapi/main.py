from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from . import crud
from .auth import (
    autenticar_usuario,
    crear_token,
    oauth2_scheme,
    verificar_token,
)
from .database import Base, engine, get_db
from .schemas import (
    OrderCreate,
    OrderResponse,
    OrderUpdate,
)

app = FastAPI(
    title="Orders API",
    version="1.0.0",
)


Base.metadata.create_all(engine)

DbSession = Annotated[
    Session,
    Depends(get_db),
]


def usuario_actual(
    token: Annotated[
        str,
        Depends(oauth2_scheme),
    ],
) -> str:
    return verificar_token(token)


UsuarioActual = Annotated[
    str,
    Depends(usuario_actual),
]


@app.post("/login")
def login(
    form: Annotated[
        OAuth2PasswordRequestForm,
        Depends(),
    ],
) -> dict[str, str]:

    valido = autenticar_usuario(
        form.username,
        form.password,
    )

    if not valido:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales incorrectas",
        )

    token = crear_token(
        form.username,
    )

    return {
        "access_token": token,
        "token_type": "bearer",
    }


@app.post(
    "/orders",
    response_model=OrderResponse,
    status_code=status.HTTP_201_CREATED,
)
def crear_order(
    datos: OrderCreate,
    session: DbSession,
    usuario: UsuarioActual,
) -> OrderResponse:
    order = crud.crear_order(
        session,
        datos,
    )

    return OrderResponse.model_validate(order)


@app.get(
    "/orders",
    response_model=list[OrderResponse],
)
def obtener_orders(
    session: DbSession,
    usuario: UsuarioActual,
) -> list[OrderResponse]:
    orders = crud.obtener_orders(session)

    return [OrderResponse.model_validate(order) for order in orders]


@app.get(
    "/orders/{order_id}",
    response_model=OrderResponse,
)
def obtener_order(
    order_id: int,
    session: DbSession,
    usuario: UsuarioActual,
) -> OrderResponse:

    order = crud.obtener_order(
        session,
        order_id,
    )

    if order is None:
        raise HTTPException(
            status_code=404,
            detail="Order no encontrada",
        )

    return OrderResponse.model_validate(order)


@app.put(
    "/orders/{order_id}",
    response_model=OrderResponse,
)
def actualizar_order(
    order_id: int,
    datos: OrderUpdate,
    session: DbSession,
    usuario: UsuarioActual,
) -> OrderResponse:

    order = crud.actualizar_order(
        session,
        order_id,
        datos,
    )

    if order is None:
        raise HTTPException(
            status_code=404,
            detail="Order no encontrada",
        )

    return OrderResponse.model_validate(order)


@app.delete(
    "/orders/{order_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def eliminar_order(
    order_id: int,
    session: DbSession,
    usuario: UsuarioActual,
) -> None:

    eliminado = crud.eliminar_order(
        session,
        order_id,
    )

    if not eliminado:
        raise HTTPException(
            status_code=404,
            detail="Order no encontrada",
        )
