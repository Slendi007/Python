class ProveedorExterno:
    def obtener_producto(
        self,
        producto_id: int,
    ) -> dict[str, object]:

        return {
            "product_id": producto_id,
            "product_name": "Laptop",
            "unit_price": 15000.0,
        }


class ProductoAdapter:
    def __init__(
        self,
        proveedor: ProveedorExterno,
    ) -> None:
        self.proveedor = proveedor

    def obtener_producto(
        self,
        producto_id: int,
    ) -> dict[str, object]:

        datos = self.proveedor.obtener_producto(producto_id)

        return {
            "id": datos["product_id"],
            "nombre": datos["product_name"],
            "precio": datos["unit_price"],
        }
