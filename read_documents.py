from pymongo import MongoClient

client = MongoClient("mongodb://mongo_db:27017/")
db = client.test_db

collection = db.users

for doc in collection.find():
    print(doc)
