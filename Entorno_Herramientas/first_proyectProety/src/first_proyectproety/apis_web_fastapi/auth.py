from datetime import datetime, timedelta, timezone

import jwt
from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordBearer

SECRET_KEY = "clave-practica-cambiar-en-produccion"

ALGORITHM = "HS256"

ACCESS_TOKEN_MINUTES = 30


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="login",
)


def autenticar_usuario(
    username: str,
    password: str,
) -> bool:
    return username == "admin" and password == "admin123"


def crear_token(
    username: str,
) -> str:
    expiracion = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_MINUTES,
    )

    payload = {
        "sub": username,
        "exp": expiracion,
    }

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM,
    )


def verificar_token(
    token: str,
) -> str:
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM],
        )

        username = payload.get("sub")

        if username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token inválido",
            )

        return str(username)

    except jwt.InvalidTokenError as error:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido o expirado",
        ) from error
