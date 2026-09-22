from sqlalchemy.orm import Session

from first_proyectproety.acceso_datos_orm.crud import (
    actualizar_usuario,
    crear_usuario,
    eliminar_usuario,
    obtener_usuario,
)


def test_crear_usuario(
    session: Session,
) -> None:
    usuario = crear_usuario(
        session,
        name="Cesar",
        email="cesar@example.com",
    )

    assert usuario.id is not None
    assert usuario.name == "Cesar"
    assert usuario.email == "cesar@example.com"


def test_obtener_usuario(
    session: Session,
) -> None:
    usuario = crear_usuario(
        session,
        name="Jared",
        email="jared@example.com",
    )

    encontrado = obtener_usuario(
        session,
        usuario.id,
    )

    assert encontrado is not None
    assert encontrado.email == "jared@example.com"


def test_actualizar_usuario(
    session: Session,
) -> None:
    usuario = crear_usuario(
        session,
        name="Gomez",
        email="gomez@example.com",
    )

    actualizado = actualizar_usuario(
        session,
        usuario.id,
        "Gomez Cesar",
    )

    assert actualizado is not None
    assert actualizado.name == "Gomez Cesar"


def test_eliminar_usuario(
    session: Session,
) -> None:
    usuario = crear_usuario(
        session,
        name="Pedro",
        email="pedro@example.com",
    )

    resultado = eliminar_usuario(
        session,
        usuario.id,
    )

    assert resultado is True

    encontrado = obtener_usuario(
        session,
        usuario.id,
    )

    assert encontrado is None
