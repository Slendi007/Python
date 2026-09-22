from .adapter import ProductoAdapter, ProveedorExterno
from .cache_decorator import cache_simple
from .strategy import CalculadoraPrecio, DescuentoDiez


@cache_simple
def calcular_doble(numero: int) -> int:
    print(f"Calculando doble de {numero}")

    return numero * 2


def main() -> None:
    print("--- Strategy ---")

    calculadora = CalculadoraPrecio(DescuentoDiez())

    precio = calculadora.calcular(100.0)

    print(f"Precio final: {precio}")

    print("\n--- Decorator ---")

    print(calcular_doble(10))
    print(calcular_doble(10))

    print("\n--- Adapter ---")

    proveedor = ProveedorExterno()

    adapter = ProductoAdapter(proveedor)

    producto = adapter.obtener_producto(1)

    print(producto)


if __name__ == "__main__":
    main()
