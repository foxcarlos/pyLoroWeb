import pymongo
from pymongo import MongoClient

conn = MongoClient('localhost', 27017)
db =  conn.test
name = db.names
item = name.find_one()
print(item['nombre'])

