import numpy as np
import pytest

from src.funciones import calculo_fitness


def test_calculo_fitness_con_datos_pequenos():
    w = np.array(
        [
            [[1, 2], [3, 4]],
            [[5, 6], [7, 8]],
        ]
    )
    x = np.array(
        [
            [[2, 1], [0, 3]],
            [[4, 2], [1, 5]],
        ]
    )
    PRA = np.array(
        [
            [10, 20],
            [30, 40],
        ]
    )
    PRE = np.array(
        [
            [1, 2],
            [3, 4],
        ]
    )

    esperado = 10 * (1 + 3) + 20 * (2 + 4) + 30 * (5 + 7) + 40 * (6 + 8)
    esperado += 1 * (2 + 0) + 2 * (1 + 3) + 3 * (4 + 1) + 4 * (2 + 5)

    assert calculo_fitness(w, x, PRA, PRE) == esperado


def test_calculo_fitness_lanza_value_error_con_dimensiones_incompatibles():
    w = np.ones((2, 2, 2))
    x = np.ones((2, 2, 2))
    PRA = np.ones((2, 3))
    PRE = np.ones((2, 3))

    with pytest.raises(ValueError, match="deben coincidir"):
        calculo_fitness(w, x, PRA, PRE)
