import math
from datetime import datetime
import pytz
def ph_from_hydrogen(concentration: float) -> float:


    if concentration <= 0:
        raise ValueError("Konzentration muss größer als 0 sein")
    return {
        "timestamp": datetime.now(pytz.timezone('Europe/Zurich')),
        "Konzentration": -math.log10(concentration)
    }