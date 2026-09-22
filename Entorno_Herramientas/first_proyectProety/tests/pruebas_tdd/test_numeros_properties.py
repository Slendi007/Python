from hypothesis import given
from hypothesis import strategies as st

from first_proyectproety.pruebas_tdd.numeros import es_par


@given(st.integers())
def test_todo_numero_multiplicado_por_dos_es_par(
    numero: int,
) -> None:
    assert es_par(numero * 2) is True
