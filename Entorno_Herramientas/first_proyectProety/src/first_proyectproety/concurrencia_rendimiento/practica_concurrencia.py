import asyncio
from concurrent.futures import ProcessPoolExecutor
from time import perf_counter

import httpx

URLS = [f"https://httpbin.org/delay/1?peticion={numero}" for numero in range(1, 5)]


def fetch_sincrono() -> None:
    print("\n--- Versión síncrona ---")

    with httpx.Client(timeout=10.0) as cliente:
        for url in URLS:
            respuesta = cliente.get(url)
            respuesta.raise_for_status()

            print(f"Respuesta: {respuesta.status_code} - {url}")


async def fetch_url(
    cliente: httpx.AsyncClient,
    url: str,
    semaforo: asyncio.Semaphore,
) -> None:
    async with semaforo:
        respuesta = await cliente.get(url)
        respuesta.raise_for_status()

        print(f"Respuesta: {respuesta.status_code} - {url}")


async def fetch_concurrente() -> None:
    print("\n--- Versión concurrente ---")

    semaforo = asyncio.Semaphore(2)

    async with httpx.AsyncClient(
        timeout=10.0,
    ) as cliente:
        tareas = [
            fetch_url(
                cliente,
                url,
                semaforo,
            )
            for url in URLS
        ]

        await asyncio.gather(*tareas)


def comparar_http() -> None:
    inicio = perf_counter()

    fetch_sincrono()

    tiempo_sincrono = perf_counter() - inicio

    inicio = perf_counter()

    asyncio.run(fetch_concurrente())

    tiempo_async = perf_counter() - inicio

    print("\n--- Comparación ---")

    print(f"Síncrono: {tiempo_sincrono:.2f} segundos")

    print(f"Concurrente: {tiempo_async:.2f} segundos")


def suma_cuadrados(limite: int) -> int:
    total = 0

    for numero in range(limite):
        total += numero * numero

    return total


def ejecutar_cpu_bound() -> None:
    print("\n--- ProcessPoolExecutor ---")

    trabajos = [
        5_000_000,
        5_000_000,
        5_000_000,
        5_000_000,
    ]

    inicio = perf_counter()

    with ProcessPoolExecutor(
        max_workers=2,
    ) as executor:
        resultados = list(
            executor.map(
                suma_cuadrados,
                trabajos,
            )
        )

    tiempo = perf_counter() - inicio

    print(f"Procesos terminados: {len(resultados)}")

    print(f"Tiempo CPU-bound: {tiempo:.2f} segundos")


def main() -> None:
    comparar_http()

    ejecutar_cpu_bound()


if __name__ == "__main__":
    main()
