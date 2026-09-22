from ..entities.order import Order


class OrderPresenter:
    @staticmethod
    def present(
        order: Order,
    ) -> dict[str, object]:
        return {
            "id": order.id,
            "cliente": order.customer,
            "producto": order.product,
            "cantidad": order.quantity,
            "mensaje": "Orden creada correctamente",
        }
