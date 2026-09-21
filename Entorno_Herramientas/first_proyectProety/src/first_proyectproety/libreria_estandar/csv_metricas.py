import csv
import json
from pathlib import Path
from statistics import mean


def leer_csv(ruta: Path) -> list[dict[str, str]]:
    registros: list[dict[str, str]] = []

    try:
        with ruta.open(mode="r", encoding="utf-8", newline="") as archivo:
            lector = csv.DictReader(archivo)

            for fila in lector:
                registros.append(fila)

    except FileNotFoundError:
        print(f"No se encontró el archivo: {ruta}")

    except OSError as error:
        print(f"Error al leer el archivo: {error}")

    return registros


def calcular_metricas(
    registros: list[dict[str, str]],
) -> dict[str, float | int]:

    ventas_totales: list[float] = []
    cantidad_total = 0

    for registro in registros:
        try:
            cantidad = int(registro["cantidad"])
            precio = float(registro["precio"])

        except ValueError, KeyError:
            print(f"Registro inválido: {registro}")
            continue

        total = cantidad * precio

        ventas_totales.append(total)
        cantidad_total += cantidad

    if not ventas_totales:
        return {
            "numero_registros": 0,
            "productos_vendidos": 0,
            "venta_total": 0.0,
            "venta_promedio": 0.0,
        }

    return {
        "numero_registros": len(ventas_totales),
        "productos_vendidos": cantidad_total,
        "venta_total": sum(ventas_totales),
        "venta_promedio": mean(ventas_totales),
    }


def exportar_json(
    datos: dict[str, float | int],
    ruta: Path,
) -> None:

    try:
        with ruta.open(mode="w", encoding="utf-8") as archivo:
            json.dump(
                datos,
                archivo,
                indent=4,
                ensure_ascii=False,
            )

    except OSError as error:
        print(f"Error al escribir JSON: {error}")


def main() -> None:

    raiz_proyecto = Path(__file__).resolve().parents[3]

    ruta_csv = raiz_proyecto / "data" / "ventas.csv"

    ruta_json = raiz_proyecto / "data" / "resultado_metricas.json"

    registros = leer_csv(ruta_csv)

    metricas = calcular_metricas(registros)

    print("Métricas calculadas:")

    for nombre, valor in metricas.items():
        print(f"{nombre}: {valor}")

    exportar_json(
        metricas,
        ruta_json,
    )

    print(f"\nJSON generado en: {ruta_json}")


if __name__ == "__main__":
    main()
