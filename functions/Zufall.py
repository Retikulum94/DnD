import random

def zufallszahl(min_zahl, max_zahl):
    """
    Generiert eine zufällige Ganzzahl zwischen min_zahl und max_zahl (inklusive).
    
    Args:
        min_zahl: Minimale Zahl (inklusive)
        max_zahl: Maximale Zahl (inklusive)
    
    Returns:
        Eine zufällige Ganzzahl im angegebenen Bereich
    """
    return random.randint(min_zahl, max_zahl)
