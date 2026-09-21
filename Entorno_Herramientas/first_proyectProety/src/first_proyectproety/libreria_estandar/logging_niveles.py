import logging
from pathlib import Path

logger = logging.getLogger(__name__)


def configurar_logging() -> None:

    raiz_proyecto = Path(__file__).resolve().parents[3]

    carpeta_logs = raiz_proyecto / "logs"

    carpeta_logs.mkdir(exist_ok=True)

    archivo_log = carpeta_logs / "aplicacion.log"

    logging.basicConfig(
        level=logging.DEBUG,
        format=("%(asctime)s | %(levelname)s | %(name)s | %(message)s"),
        handlers=[
            logging.FileHandler(
                archivo_log,
                encoding="utf-8",
            ),
            logging.StreamHandler(),
        ],
    )


def dividir(
    numero1: float,
    numero2: float,
) -> float | None:

    logger.debug(
        "Intentando dividir %s entre %s",
        numero1,
        numero2,
    )

    if numero2 == 0:
        logger.error("---No se puede dividir entre cero---")

        return None

    resultado = numero1 / numero2

    logger.info("---División realizada correctamente---")

    return resultado


def main() -> None:

    configurar_logging()

    logger.debug("---Mensaje de depuración---")

    logger.info("---La aplicación comenzó---")

    logger.warning("---Este es un mensaje de advertencia---")

    resultado = dividir(
        10,
        2,
    )

    logger.info(
        "Resultado: %s",
        resultado,
    )

    dividir(
        10,
        0,
    )

    logger.critical("---Ejemplo de mensaje crítico---")

    logger.info("---La aplicación terminó---")


if __name__ == "__main__":
    main()
