from first_proyectproety.patrones_diseño.adapter import (
    ProductoAdapter,
    ProveedorExterno,
)


def test_adapter_convierte_formato() -> None:
    proveedor = ProveedorExterno()

    adapter = ProductoAdapter(proveedor)

    producto = adapter.obtener_producto(1)

    assert producto == {
        "id": 1,
        "nombre": "Laptop",
        "precio": 15000.0,
    }
