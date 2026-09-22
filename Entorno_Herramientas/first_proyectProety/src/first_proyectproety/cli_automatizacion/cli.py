import httpx
import typer

app = typer.Typer()

API_URL = "http://127.0.0.1:8000"


def obtener_token() -> str:
    respuesta = httpx.post(
        f"{API_URL}/login",
        data={
            "username": "admin",
            "password": "admin123",
        },
    )

    respuesta.raise_for_status()

    return str(respuesta.json()["access_token"])


def obtener_headers() -> dict[str, str]:
    token = obtener_token()

    return {
        "Authorization": f"Bearer {token}",
    }


@app.command("list")
def listar_orders() -> None:
    respuesta = httpx.get(
        f"{API_URL}/orders",
        headers=obtener_headers(),
    )

    respuesta.raise_for_status()

    orders = respuesta.json()

    if not orders:
        typer.echo("No hay órdenes.")
        return

    for order in orders:
        typer.echo(
            f"{order['id']} | "
            f"{order['customer']} | "
            f"{order['product']} | "
            f"{order['quantity']} | "
            f"${order['price']}"
        )


@app.command("create")
def crear_order(
    customer: str,
    product: str,
    quantity: int,
    price: float,
) -> None:
    respuesta = httpx.post(
        f"{API_URL}/orders",
        headers=obtener_headers(),
        json={
            "customer": customer,
            "product": product,
            "quantity": quantity,
            "price": price,
        },
    )

    respuesta.raise_for_status()

    order = respuesta.json()

    typer.echo(f"Orden {order['id']} creada correctamente.")


@app.command("delete")
def borrar_order(
    order_id: int,
) -> None:
    respuesta = httpx.delete(
        f"{API_URL}/orders/{order_id}",
        headers=obtener_headers(),
    )

    if respuesta.status_code == 404:
        typer.echo("La orden no existe.")
        raise typer.Exit(code=1)

    respuesta.raise_for_status()

    typer.echo(f"Orden {order_id} eliminada.")


def main() -> None:
    app()


if __name__ == "__main__":
    main()
