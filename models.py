from pymongo import MongoClient

client = MongoClient('localhost', 27017)

currencies = client.projectDB.currencies
