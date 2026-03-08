import random
from fractions import Fraction

class ZufallszahlenGenerator:
    
    @staticmethod
    def ganze_zahl(von: int, bis: int) -> int:
        return random.randint(von, bis)
    
    @staticmethod
    def rationale_zahl(von: float = 0.0, bis: float = 1.0) -> float:
        return random.uniform(von, bis)
    
    @staticmethod
    def bruch(von_zaehler: int = 0, bis_zaehler: int = 10, 
          von_nenner: int = 1, bis_nenner: int = 10) -> Fraction:
        zaehler = random.randint(von_zaehler, bis_zaehler)
        nenner = random.randint(von_nenner, bis_nenner)
        return Fraction(zaehler, nenner)
