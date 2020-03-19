from pymongo import MongoClient
client = MongoClient()
client = MongoClient("mongodb://localhost:27017/")
mydatabase = client.testdb
mycollection = mydatabase.myTable
record = {
    'title': 'MongoDB and Python',
    'description': 'MongoDB is no SQL database',
    'tags': ['mongodb', 'database', 'NoSQL'],
    'viewers': 104
}
rec = mycollection.insert_one(record)