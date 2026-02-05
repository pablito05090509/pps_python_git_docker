from pymongo import MongoClient

client = MongoClient("mongodb://mongo_db:27017/")
db = client.test_db
collection = db.users

# Borrar un documento
result = collection.delete_one({"nombre": "Luis"})
print(f"Documentos eliminados: {result.deleted_count}")

# Borrar todos los documentos (cuidado)
# result = collection.delete_many({})
# print(f"Documentos eliminados: {result.deleted_count}")
