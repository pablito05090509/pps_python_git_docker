from pymongo import MongoClient
import random

def get_collection():
    client = MongoClient("mongodb://mongo_db:27017/")
    db = client.bayeta_db
    return db.frases

def init_frases():
    frases = [
        {"frase": "La fortuna sonríe a los valientes"},
        {"frase": "Hoy es un buen día para aprender algo nuevo"},
        {"frase": "La paciencia trae recompensas"},
        {"frase": "Tu esfuerzo dará frutos pronto"},
        {"frase": "Sonríe y el mundo sonreirá contigo"}
    ]
    col = get_collection()
    col.delete_many({})  # Borra lo que haya para no duplicar
    col.insert_many(frases)
    print("MongoDB inicializado con frases")

def get_frases(n):
    col = get_collection()
    all_frases = list(col.find({}))
    if not all_frases:
        return ["No hay frases disponibles"]
    return [random.choice(all_frases)["frase"] for _ in range(n)]

if __name__ == "__main__":
    init_frases()
