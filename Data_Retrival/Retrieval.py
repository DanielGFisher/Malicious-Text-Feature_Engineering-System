from fastapi import FastAPI
from pymongo import MongoClient
import os

app = FastAPI(title="Tweet Retrieval API")

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(MONGO_URI)
db = client["IranTweetsDB"]

@app.get("/antisemitic")
def get_antisemitic():
    """
    Return all antisemitic tweets
    """
    collection = db["tweets_antisemitic"]
    docs = list(collection.find({}, {"_id": 0}))
    return docs

@app.get("/not_antisemitic")
def get_not_antisemitic():
    """
    Return all non-antisemitic tweets
    """
    collection = db["tweets_not_antisemitic"]
    docs = list(collection.find({}, {"_id": 0}))
    return docs