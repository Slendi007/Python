import logging
import time
from pathlib import Path
from typing import Any

import httpx

# Configuración
TIMEOUT = httpx.Timeout(
    connect=5.0,
    read=10.0,
    write=10.0,
    pool=5.0,
)

MAX_REINTENTOS = 3
TAMANO_BLOQUE = 64 * 1024  # 64 KB


# Logging
logging.basicConfig(
    level=logging.INFO,
    format=("%(asctime)s | %(levelname)s | %(name)s | %(message)s"),
)

logger = logging.getLogger(__name__)


# Cliente HTTP
def crear_cliente() -> httpx.Client:
    """Crea y configura un cliente HTTPX."""

    return httpx.Client(
        timeout=TIMEOUT,
        follow_redirects=True,
    )


# Obtener JSON
def obtener_json(
    cliente: httpx.Client,
    url: str,
    reintentos: int = MAX_REINTENTOS,
) -> dict[str, Any] | None:
    """Realiza una petición GET y devuelve la respuesta JSON."""

    for intento in range(1, reintentos + 1):
        try:
            logger.info(
                "GET %s - intento %s/%s",
                url,
                intento,
                reintentos,
            )

            respuesta = cliente.get(url)

            respuesta.raise_for_status()

            datos: dict[str, Any] = respuesta.json()

            logger.info("Petición realizada correctamente.")

            return datos

        except (
            httpx.TimeoutException,
            httpx.NetworkError,
        ) as error:
            logger.warning(
                "Error de conexión: %s",
                error,
            )

            if intento < reintentos:
                espera = 2 ** (intento - 1)

                logger.info(
                    "Reintentando en %s segundo(s)...",
                    espera,
                )

                time.sleep(espera)

        except httpx.HTTPStatusError as error:
            logger.error(
                "Error HTTP %s al consultar %s",
                error.response.status_code,
                url,
            )

            return None

        except ValueError as error:
            logger.error(
                "La respuesta no contiene JSON válido: %s",
                error,
            )

            return None

    logger.error(
        "Se agotaron los %s intentos.",
        reintentos,
    )

    return None


# Descargar archivo mediante streaming
def descargar_archivo(
    cliente: httpx.Client,
    url: str,
    destino: Path,
    reintentos: int = MAX_REINTENTOS,
) -> bool:
    "--Descarga un archivo por streaming y lo guarda en disco--"

    destino.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    for intento in range(1, reintentos + 1):
        try:
            logger.info(
                "Descargando %s - intento %s/%s",
                url,
                intento,
                reintentos,
            )

            with cliente.stream(
                "GET",
                url,
            ) as respuesta:
                respuesta.raise_for_status()

                with destino.open("wb") as archivo:
                    for bloque in respuesta.iter_bytes(
                        chunk_size=TAMANO_BLOQUE,
                    ):
                        archivo.write(bloque)

            logger.info(
                "Descarga completada: %s",
                destino,
            )

            return True

        except (
            httpx.TimeoutException,
            httpx.NetworkError,
        ) as error:
            logger.warning(
                "Problema durante la descarga: %s",
                error,
            )

            destino.unlink(missing_ok=True)

            if intento < reintentos:
                espera = 2 ** (intento - 1)

                logger.info(
                    "Reintentando en %s segundo(s)...",
                    espera,
                )

                time.sleep(espera)

        except httpx.HTTPStatusError as error:
            logger.error(
                "Error HTTP %s durante la descarga.",
                error.response.status_code,
            )

            destino.unlink(missing_ok=True)

            return False

        except OSError as error:
            logger.error(
                "Error al escribir el archivo: %s",
                error,
            )

            destino.unlink(missing_ok=True)

            return False

    logger.error("No fue posible descargar el archivo.")

    return False


# Programa principal
def main() -> None:
    raiz_proyecto = Path(__file__).resolve().parents[3]

    carpeta_descargas = raiz_proyecto / "descargas"

    # API de prueba
    url_api = "https://httpbin.org/get"

    # Descarga real de 1 MB mediante streaming
    url_archivo = "https://httpbin.org/stream-bytes/1048576"

    archivo_destino = carpeta_descargas / "archivo_stream.bin"

    logger.info("Iniciando práctica de HTTPX.")

    with crear_cliente() as cliente:
        # Prueba 1: petición JSON
        datos = obtener_json(
            cliente,
            url_api,
        )

        if datos is not None:
            logger.info(
                "URL recibida desde la API: %s",
                datos.get("url"),
            )

        # Prueba 2: descarga por streaming
        descargado = descargar_archivo(
            cliente,
            url_archivo,
            archivo_destino,
        )

        if descargado:
            tamano = archivo_destino.stat().st_size

            logger.info(
                "Tamaño descargado: %s bytes",
                tamano,
            )

    logger.info("Práctica finalizada.")


if __name__ == "__main__":
    main()
