from fastapi import FastAPI
from pymongo import MongoClient
import os

app = FastAPI(title="Tweet Retrieval API")

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(MONGO_URI)
db = client["antisemitic_tweets"]  # Match Persister DB

def serialize_doc(doc):
    doc["id"] = str(doc["_id"])
    del doc["_id"]
    return doc

@app.get("/antisemitic")
def get_antisemitic():
    """
    Return all antisemitic tweets
    """
    collection = db["tweets_antisemitic"]
    docs = [serialize_doc(doc) for doc in collection.find({})]
    return docs

@app.get("/not_antisemitic")
def get_not_antisemitic():
    """
    Return all non-antisemitic tweets
    """
    collection = db["tweets_not_antisemitic"]
    docs = [serialize_doc(doc) for doc in collection.find({})]
    return docs
