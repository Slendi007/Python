from first_proyectproety.patrones_diseño.strategy import (
    CalculadoraPrecio,
    DescuentoDiez,
    DescuentoVeinte,
    PrecioNormal,
)


def test_precio_normal() -> None:
    calculadora = CalculadoraPrecio(PrecioNormal())

    resultado = calculadora.calcular(100)

    assert resultado == 100


def test_descuento_diez() -> None:
    calculadora = CalculadoraPrecio(DescuentoDiez())

    resultado = calculadora.calcular(100)

    assert resultado == 90


def test_descuento_veinte() -> None:
    calculadora = CalculadoraPrecio(DescuentoVeinte())

    resultado = calculadora.calcular(100)

    assert resultado == 80
