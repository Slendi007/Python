from first_proyectproety.objetos_modelos_datos.modelos import Order, OrderIn, OrderOut


def order_in_to_entity(order_in: OrderIn) -> Order:
    "----Convierte OrderIn en una entidad Order----"

    return Order(
        id=order_in.id,
        product=order_in.product,
        quantity=order_in.quantity,
        unit_price=order_in.unit_price,
        tax_rate=order_in.tax_rate,
    )


def order_to_out(order: Order) -> OrderOut:
    "----Convierte una entidad Order en OrderOut----"

    return OrderOut(
        id=order.id,
        product=order.product,
        quantity=order.quantity,
        unit_price=order.unit_price,
        subtotal=order.subtotal,
        tax=order.tax,
        total=order.total,
    )
