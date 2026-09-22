from pathlib import Path

import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

RAIZ_PROYECTO = Path(__file__).resolve().parents[3]

RUTA_CSV = RAIZ_PROYECTO / "data" / "clientes.csv"

RUTA_MODELO = RAIZ_PROYECTO / "modelos" / "clasificador_clientes.joblib"


def cargar_datos() -> pd.DataFrame:
    datos = pd.read_csv(RUTA_CSV)

    print("Datos originales:")
    print(datos.head())

    return datos


def limpiar_datos(
    datos: pd.DataFrame,
) -> pd.DataFrame:
    datos = datos.copy()

    datos = datos.drop_duplicates()

    columnas = [
        "edad",
        "ingresos",
        "visitas",
        "compro",
    ]

    for columna in columnas:
        datos[columna] = pd.to_numeric(
            datos[columna],
            errors="coerce",
        )

    datos = datos.dropna()

    print(f"\nRegistros después de limpiar: {len(datos)}")

    return datos


def entrenar_modelo(
    datos: pd.DataFrame,
) -> Pipeline:
    caracteristicas = [
        "edad",
        "ingresos",
        "visitas",
    ]

    x = datos[caracteristicas]
    y = datos["compro"].astype(int)

    x_train, x_test, y_train, y_test = train_test_split(
        x,
        y,
        test_size=0.25,
        random_state=42,
        stratify=y,
    )

    modelo = Pipeline(
        steps=[
            (
                "scaler",
                StandardScaler(),
            ),
            (
                "clasificador",
                LogisticRegression(),
            ),
        ]
    )

    modelo.fit(
        x_train,
        y_train,
    )

    predicciones = modelo.predict(x_test)

    precision = accuracy_score(
        y_test,
        predicciones,
    )

    print(f"Accuracy: {precision:.2f}")

    return modelo


def guardar_modelo(
    modelo: Pipeline,
) -> None:
    RUTA_MODELO.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    joblib.dump(
        modelo,
        RUTA_MODELO,
    )

    print(f"Modelo guardado en: {RUTA_MODELO}")


def main() -> None:
    datos = cargar_datos()

    datos_limpios = limpiar_datos(datos)

    modelo = entrenar_modelo(datos_limpios)

    guardar_modelo(modelo)


if __name__ == "__main__":
    main()
