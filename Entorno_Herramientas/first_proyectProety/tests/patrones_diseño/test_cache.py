from first_proyectproety.patrones_diseño.cache_decorator import (
    cache_simple,
)


def test_cache_evitar_calculo_repetido() -> None:
    contador = 0

    @cache_simple
    def calcular(numero: int) -> int:
        nonlocal contador

        contador += 1

        return numero * 2

    resultado1 = calcular(10)
    resultado2 = calcular(10)

    assert resultado1 == 20
    assert resultado2 == 20

    assert contador == 1
