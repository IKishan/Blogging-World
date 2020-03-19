from pymongo import MongoClient
conn = MongoClient()
conn = MongoClient("mongodb://localhost:27017/")
database = conn.bloggingWorld