import random

def frotar(n_frases: int = 1) -> list:
    frases = []
    try:
        with open("frases.txt", "r", encoding="utf-8") as f:
            lineas = [line.strip() for line in f.readlines() if line.strip()]
            for _ in range(n_frases):
                frases.append(random.choice(lineas))
    except FileNotFoundError:
        frases = ["No hay frases disponibles"]
    return frases
from mongo_init import get_frases

def frotar(n_frases: int = 1) -> list:
    return get_frases(n_frases)
