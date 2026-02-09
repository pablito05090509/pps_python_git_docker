import time
from pymongo import MongoClient, errors

def get_db():
    client = MongoClient("mongodb://mongo_db:27017/", serverSelectionTimeoutMS=5000)
    return client.bayeta_db

def init_frases(retries=10, delay=2):
    """Espera a que MongoDB esté listo y luego inserta las frases iniciales"""
    db = None
    for i in range(retries):
        try:
            db = get_db()
            db.command("ping")  # Verifica que MongoDB responde
            break
        except errors.ServerSelectionTimeoutError:
            print(f"[mongo_init] MongoDB no listo, reintentando en {delay} segundos...")
            time.sleep(delay)
    else:
        raise Exception("No se pudo conectar a MongoDB")

    coleccion = db.frases
    if coleccion.count_documents({}) == 0:
        coleccion.insert_many([
            {"frase": "La fortuna sonríe a los valientes"},
            {"frase": "La paciencia trae recompensas"},
            {"frase": "Sonríe y el mundo sonreirá contigo"}
        ])
        print("[mongo_init] MongoDB inicializado con frases")
