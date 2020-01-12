import pymongo
import os

MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "beerTime"
COLLECTION_NAME = "beerTime"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to mongodb: %s") % e

conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

# new_doc = {'name': 'mongo-beer', 'brewery': 'mongo-brewery', 'type': 'ipa'}
# new_docs = [{'first': 'dict'}, {'second': 'dict'}]
# use insert_many for multiple inserts and insert_one for one...
# use coll.remove to remove values



coll.insert(new_doc)

documents = coll.find()

for doc in documents:
    print(doc)
