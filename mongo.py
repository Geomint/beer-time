import pymongo
import os

MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "beerTime"
COLLECTION_NAME = "beerTime"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to mongodb: %s") % e

