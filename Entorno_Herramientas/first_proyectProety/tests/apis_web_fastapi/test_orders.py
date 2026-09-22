from fastapi.testclient import TestClient


def obtener_headers(
    client: TestClient,
) -> dict[str, str]:

    respuesta = client.post(
        "/login",
        data={
            "username": "admin",
            "password": "admin123",
        },
    )

    assert respuesta.status_code == 200

    token = respuesta.json()["access_token"]

    return {"Authorization": (f"Bearer {token}")}


def test_crud_orders(
    client: TestClient,
) -> None:

    headers = obtener_headers(client)

    # CREATE

    respuesta = client.post(
        "/orders",
        headers=headers,
        json={
            "customer": "Cesar",
            "product": "Laptop",
            "quantity": 1,
            "price": 15000,
        },
    )

    assert respuesta.status_code == 201

    datos = respuesta.json()

    order_id = datos["id"]

    # READ

    respuesta = client.get(
        f"/orders/{order_id}",
        headers=headers,
    )

    assert respuesta.status_code == 200

    assert respuesta.json()["product"] == "Laptop"

    # UPDATE

    respuesta = client.put(
        f"/orders/{order_id}",
        headers=headers,
        json={
            "customer": "Cesar",
            "product": "Monitor",
            "quantity": 2,
            "price": 4500,
        },
    )

    assert respuesta.status_code == 200

    assert respuesta.json()["product"] == "Monitor"

    # DELETE

    respuesta = client.delete(
        f"/orders/{order_id}",
        headers=headers,
    )

    assert respuesta.status_code == 204

    # Comprobar eliminación

    respuesta = client.get(
        f"/orders/{order_id}",
        headers=headers,
    )

    assert respuesta.status_code == 404


def test_order_invalida(
    client: TestClient,
) -> None:

    headers = obtener_headers(client)

    respuesta = client.post(
        "/orders",
        headers=headers,
        json={
            "customer": "Cesar",
            "product": "Laptop",
            "quantity": -5,
            "price": 15000,
        },
    )

    assert respuesta.status_code == 422


def test_orders_sin_token(
    client: TestClient,
) -> None:

    respuesta = client.get("/orders")

    assert respuesta.status_code == 401
