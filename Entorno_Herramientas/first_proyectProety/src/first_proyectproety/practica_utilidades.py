import random
import time

from first_proyectproety.utilidades import Temporizador, por_lotes, reintentar


@reintentar(max_intentos=4, espera_inicial=1)
def consultar_servidor() -> str:

    if random.random() < 0.7:
        raise ConnectionError("No se pudo conectar con el servidor.")

    return "Datos recibidos correctamente."


def procesar_lote(lote: list[int]) -> None:

    print(f"Procesando lote: {lote}")
    time.sleep(0.5)


def main() -> None:
    datos: list[int] = list(range(1, 11))

    print("=== GENERADOR POR LOTES ===")

    with Temporizador():
        for lote in por_lotes(datos, 3):
            procesar_lote(lote)

    print("\n=== DECORADOR DE REINTENTOS ===")

    try:
        resultado = consultar_servidor()
        print(resultado)
    except ConnectionError as error:
        print(f"Error definitivo: {error}")


if __name__ == "__main__":
    main()
