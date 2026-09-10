import json
from pathlib import Path


def leer_json(ruta: str) -> list[dict]:

    archivo = Path(ruta)

    if not archivo.exists():
        raise FileNotFoundError(f"No se encontró el archivo: {ruta}")

    try:
        with archivo.open("r", encoding="utf-8") as archivo_json:
            datos = json.load(archivo_json)
    except json.JSONDecodeError as error:
        raise ValueError(
            f"El archivo JSON no tiene un formato válido: {error}"
        ) from error
    except OSError as error:
        raise OSError(f"No se pudo leer el archivo: {error}") from error

    if not isinstance(datos, list):
        raise ValueError("El JSON debe contener una lista de registros.")

    return datos


def filtrar_usuarios(usuarios: list[dict]) -> list[dict]:
    """Devuelve únicamente los usuarios activos."""
    return [usuario for usuario in usuarios if usuario.get("activo") is True]


def agregar_ventas(usuarios: list[dict]) -> float:
    """Calcula el total de ventas de los usuarios."""
    return sum(usuario.get("ventas", 0) for usuario in usuarios)


def main() -> None:
    ruta = "data/usuarios.json"

    try:
        usuarios = leer_json(ruta)
        usuarios_activos = filtrar_usuarios(usuarios)
        total_ventas = agregar_ventas(usuarios_activos)

        print(f"Usuarios encontrados: {len(usuarios)}")
        print(f"Usuarios activos: {len(usuarios_activos)}")
        print(f"Ventas totales de usuarios activos: ${total_ventas:,.2f}")

        print("\nUsuarios activos:")
        for usuario in usuarios_activos:
            print(
                f"- {usuario.get('nombre')} | "
                f"{usuario.get('ciudad')} | "
                f"Ventas: ${usuario.get('ventas', 0):,.2f}"
            )

    except (FileNotFoundError, ValueError, OSError) as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
