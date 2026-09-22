from collections.abc import Callable
from functools import wraps
from typing import TypeVar

T = TypeVar("T")


def cache_simple(
    funcion: Callable[[int], T],
) -> Callable[[int], T]:

    cache: dict[int, T] = {}

    @wraps(funcion)
    def wrapper(valor: int) -> T:
        if valor in cache:
            return cache[valor]

        resultado = funcion(valor)

        cache[valor] = resultado

        return resultado

    return wrapper
