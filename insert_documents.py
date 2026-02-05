from pymongo import MongoClient

# Conexión
client = MongoClient("mongodb://mongo_db:27017/")
db = client.test_db  # Base de datos

# Crear colección
collection = db.users

# Insertar documentos
collection.insert_many([
    {"nombre": "Pablo", "edad": 30, "profesion": "developer"},
    {"nombre": "Ana", "edad": 25, "profesion": "designer"},
    {"nombre": "Luis", "edad": 35, "profesion": "manager"}
])

print("Documentos insertados correctamente.")
