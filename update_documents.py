from pymongo import MongoClient

client = MongoClient("mongodb://mongo_db:27017/")
db = client.test_db
collection = db.users

# Actualizar un documento: cambiar edad de Pablo a 31
result = collection.update_one(
    {"nombre": "Pablo"},  # filtro
    {"$set": {"edad": 31}}  # actualización
)
print(f"Documentos modificados: {result.modified_count}")

# Actualizar varios documentos: sumar 1 año a todos los usuarios
result = collection.update_many(
    {},
    {"$inc": {"edad": 1}}
)
print(f"Documentos modificados en total: {result.modified_count}")

