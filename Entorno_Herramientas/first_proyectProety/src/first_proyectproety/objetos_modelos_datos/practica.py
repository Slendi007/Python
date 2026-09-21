from first_proyectproety.objetos_modelos_datos.conversiones import (
    order_in_to_entity,
    order_to_out,
)
from first_proyectproety.objetos_modelos_datos.modelos import Order, OrderIn


def main() -> None:
    order_input = OrderIn(
        id=1,
        product="Laptop",
        quantity=2,
        unit_price=15000,
    )

    order = order_in_to_entity(order_input)

    order_output = order_to_out(order)

    print("=== ORDER ===")
    print(order)

    print("\n=== CÁLCULOS ===")
    print(f"Subtotal: ${order.subtotal:,.2f}")
    print(f"Impuesto: ${order.tax:,.2f}")
    print(f"Total: ${order.total:,.2f}")

    print("\n=== ORDER OUT ===")
    print(order_output.model_dump())

    print("\n=== COMPARACIÓN ===")

    otra_order = Order(
        id=2,
        product="Monitor",
        quantity=1,
        unit_price=5000,
    )

    print(f"Order 1 < Order 2: {order < otra_order}")
    print(f"Order 1 == Order 2: {order == otra_order}")


if __name__ == "__main__":
    main()
