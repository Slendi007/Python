from pydantic import BaseModel, ConfigDict, Field


class OrderBase(BaseModel):
    customer: str = Field(
        min_length=2,
        max_length=100,
    )

    product: str = Field(
        min_length=2,
        max_length=100,
    )

    quantity: int = Field(
        gt=0,
    )

    price: float = Field(
        gt=0,
    )


class OrderCreate(OrderBase):
    pass


class OrderUpdate(OrderBase):
    pass


class OrderResponse(OrderBase):
    id: int

    model_config = ConfigDict(
        from_attributes=True,
    )
