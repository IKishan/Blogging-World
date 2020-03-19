from pymongo import MongoClient
try:
    conn = MongoClient()
    print("Connected!!")
except:
    print("Connection failed...")

db = conn.testdb
collection = db.myTable
cursor = collection.find()
for record in cursor:
    print(record)