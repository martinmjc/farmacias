import numpy as np


def calculo_fitness(w, x, PRA, PRE):
    """Calcula el costo total de compras del modelo matematico."""
    w = np.asarray(w)
    x = np.asarray(x)
    PRA = np.asarray(PRA)
    PRE = np.asarray(PRE)

    if w.ndim != 3:
        raise ValueError("w debe tener forma (n, m, T).")
    if x.ndim != 3:
        raise ValueError("x debe tener forma (n, m, T).")
    if PRA.ndim != 2:
        raise ValueError("PRA debe tener forma (n, T).")
    if PRE.ndim != 2:
        raise ValueError("PRE debe tener forma (n, T).")
    if w.shape != x.shape:
        raise ValueError(
            f"w y x deben tener la misma forma (n, m, T); se recibio {w.shape} y {x.shape}."
        )
    if PRA.shape != PRE.shape:
        raise ValueError(
            f"PRA y PRE deben tener la misma forma (n, T); se recibio {PRA.shape} y {PRE.shape}."
        )

    n, _, T = w.shape
    if PRA.shape != (n, T):
        raise ValueError(
            "Las dimensiones de PRA y PRE deben coincidir con n y T de w/x; "
            f"se esperaba {(n, T)} y se recibio {PRA.shape}."
        )

    costo_planificado = np.sum(PRA[:, np.newaxis, :] * w)
    costo_extra = np.sum(PRE[:, np.newaxis, :] * x)

    return (costo_planificado + costo_extra).item()
