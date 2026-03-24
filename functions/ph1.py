import math
from datetime import datetime
import pytz
def ph_from_hydrogen(concentration: float) -> float:
    if concentration <= 0.000000000000001:
        raise ValueError("Höher als ")
    return -math.log10(concentration)