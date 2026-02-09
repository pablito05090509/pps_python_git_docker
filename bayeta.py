import random
from mongo_init import get_db

def frotar(n_frases: int = 1):
    db = get_db()
    coleccion = db.frases
    all_frases = list(coleccion.find({}, {"_id": 0, "frase": 1}))
    if not all_frases:
        raise Exception("No hay frases en la base de datos")
    return [random.choice(all_frases)["frase"] for _ in range(n_frases)]

def agregar_frases(frases: list):
    if not frases:
        return 0
    db = get_db()
    coleccion = db.frases
    documentos = [{"frase": f} for f in frases]
    resultado = coleccion.insert_many(documentos)
    return len(resultado.inserted_ids)
