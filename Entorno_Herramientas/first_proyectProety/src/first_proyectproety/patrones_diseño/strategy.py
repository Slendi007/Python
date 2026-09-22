from typing import Protocol


class EstrategiaPrecio(Protocol):
    def calcular(self, precio: float) -> float: ...


class PrecioNormal:
    def calcular(self, precio: float) -> float:
        return precio


class DescuentoDiez:
    def calcular(self, precio: float) -> float:
        return precio * 0.90


class DescuentoVeinte:
    def calcular(self, precio: float) -> float:
        return precio * 0.80


class CalculadoraPrecio:
    def __init__(
        self,
        estrategia: EstrategiaPrecio,
    ) -> None:
        self.estrategia = estrategia

    def calcular(self, precio: float) -> float:
        return self.estrategia.calcular(precio)
