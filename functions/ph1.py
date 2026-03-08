# functions/ph1.py

import math

def ph_from_hydrogen(concentration: float) -> float:
    """
    Rückgabe des pH-Werts zu einer gegebenen [H+]‑Konzentration
    (in mol/L).  Für Konzentrationen ≤ 0 wird ein ValueError geworfen.

    Beispiel:
        >>> ph_from_hydrogen(1e-7)
        7.0
    """
    if concentration <= 0:
        raise ValueError("Konzentration muss größer als 0 sein")
    return -math.log10(concentration)
