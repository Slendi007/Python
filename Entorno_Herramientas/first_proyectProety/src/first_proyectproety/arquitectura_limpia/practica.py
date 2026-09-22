from .adapters.memory_uow import (
    MemoryUnitOfWork,
)
from .adapters.presenter import (
    OrderPresenter,
)
from .application.create_order import (
    CreateOrder,
)
from .application.event_handlers import (
    OrderCreatedHandler,
)


def main() -> None:
    uow = MemoryUnitOfWork()

    event_handler = OrderCreatedHandler()

    use_case = CreateOrder(
        uow,
        event_handler,
    )

    order = use_case.execute(
        order_id=1,
        customer="Cesar",
        product="Laptop",
        quantity=2,
    )

    respuesta = OrderPresenter.present(order)

    print(respuesta)


if __name__ == "__main__":
    main()
