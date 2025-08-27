from pymongo import MongoClient
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

class ConnectionDB:
    def __init__(self, db_name = "IranMalDB", collection_name = "tweets"):

        mongo_uri_conn = os.getenv("CONNECTION_STRING")
        uri = mongo_uri_conn

        # connecting to server
        self.client = MongoClient(uri)
        # select a DB
        self.db = self.client[db_name]
        # select collection
        self.collection = self.db[collection_name]


    def get_data_batch(self, batch_size=100):
        cursor = self.collection.find({}).sort("CreateDate", 1).limit(batch_size)
        return list(cursor)

#for testing
# c = ConnectionDB()
# print(c.get_data_batch())

