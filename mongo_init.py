from pymongo import MongoClient

def get_collection():
    client = MongoClient("mongodb://mongo_db:27017/")
    db = client["bayeta_db"]
    collection = db["frases"]
    return collection

def init_frases():
    collection = get_collection()
    frases = [
        "Hoy es tu día de suerte",
        "Confía en tu intuición",
        "Una sorpresa agradable te espera",
        "Sonríe, todo saldrá bien"
    ]
    for f in frases:
        if not collection.find_one({"frase": f}):
            collection.insert_one({"frase": f})

def get_frases(n):
    collection = get_collection()
    all_frases = list(collection.find({}, {"_id": 0, "frase": 1}))
    import random
    return [random.choice(all_frases)["frase"] for _ in range(n)]

if __name__ == "__main__":
    init_frases()
    print(get_frases(3))
