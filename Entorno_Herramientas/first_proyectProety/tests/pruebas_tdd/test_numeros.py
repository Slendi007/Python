from first_proyectproety.pruebas_tdd.numeros import es_par


def test_numero_par() -> None:
    assert es_par(4) is True


def test_numero_impar() -> None:
    assert es_par(5) is False
