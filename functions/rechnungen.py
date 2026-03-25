from datetime import datetime
import pytz


def add(a, b):
    return a + b
    

def subtract(a, b):
    return a - b

def square(a):
    return a * a

def root(a, b):
    return a ** (1/b)


## return {         "timestamp": datetime.now(pytz.timezone('Europe/Zurich')),      "Ergebnis": a+b     }