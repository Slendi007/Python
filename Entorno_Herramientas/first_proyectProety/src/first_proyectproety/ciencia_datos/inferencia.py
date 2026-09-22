from pathlib import Path

import joblib
import pandas as pd
from sklearn.pipeline import Pipeline

RAIZ_PROYECTO = Path(__file__).resolve().parents[3]

RUTA_MODELO = RAIZ_PROYECTO / "modelos" / "clasificador_clientes.joblib"


def cargar_modelo() -> Pipeline:
    modelo: Pipeline = joblib.load(RUTA_MODELO)

    return modelo


def predecir(
    modelo: Pipeline,
    edad: int,
    ingresos: float,
    visitas: int,
) -> int:
    datos = pd.DataFrame(
        [
            {
                "edad": edad,
                "ingresos": ingresos,
                "visitas": visitas,
            }
        ]
    )

    prediccion = modelo.predict(datos)

    return int(prediccion[0])


def main() -> None:
    modelo = cargar_modelo()

    resultado = predecir(
        modelo=modelo,
        edad=38,
        ingresos=21000,
        visitas=6,
    )

    if resultado == 1:
        print("Predicción: el cliente probablemente comprará.")
    else:
        print("Predicción: el cliente probablemente no comprará.")


if __name__ == "__main__":
    main()
