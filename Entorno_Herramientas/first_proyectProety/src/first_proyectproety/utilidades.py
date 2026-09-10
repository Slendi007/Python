import time
from collections.abc import Callable, Iterator
from functools import wraps
from time import perf_counter
from typing import ParamSpec, TypeVar

P = ParamSpec("P")
T = TypeVar("T")


def reintentar(
    max_intentos: int = 3,
    espera_inicial: float = 1.0,
) -> Callable[[Callable[P, T]], Callable[P, T]]:

    def decorador(funcion: Callable[P, T]) -> Callable[P, T]:
        @wraps(funcion)
        def envoltura(*args: P.args, **kwargs: P.kwargs) -> T:
            espera = espera_inicial

            for intento in range(1, max_intentos + 1):
                try:
                    return funcion(*args, **kwargs)
                except Exception as error:
                    if intento == max_intentos:
                        raise

                    print(
                        f"Intento {intento} fallido: {error}. "
                        f"Reintentando en {espera:.1f} segundos..."
                    )

                    time.sleep(espera)
                    espera *= 2

            raise RuntimeError("No se pudo completar la operación.")

        return envoltura

    return decorador


def por_lotes(
    elementos: list[T],
    tamano_lote: int,
) -> Iterator[list[T]]:

    if tamano_lote <= 0:
        raise ValueError("El tamaño del lote debe ser mayor que cero.")

    for inicio in range(0, len(elementos), tamano_lote):
        yield elementos[inicio : inicio + tamano_lote]


class Temporizador:
    def __enter__(self) -> "Temporizador":
        self.inicio = perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        self.fin = perf_counter()
        self.duracion = self.fin - self.inicio

        print(f"Tiempo transcurrido: {self.duracion:.4f} segundos")
