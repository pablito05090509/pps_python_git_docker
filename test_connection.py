from pymongo import MongoClient

client = MongoClient("mongodb://mongo_db:27017/")
db = client.test_db

print("Bases de datos existentes:", client.list_database_names())
