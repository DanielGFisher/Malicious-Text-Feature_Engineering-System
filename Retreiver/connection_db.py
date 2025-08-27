from pymongo import MongoClient
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

class ConnectionDB:
    def __init__(self, db_name, collection_name):

        mongo_uri_conn = os.getenv("CONN_STRING")
        uri = mongo_uri_conn

        # connecting to server
        self.client = MongoClient(uri)
        # select a DB
        self.db = self.client[db_name]
        # select collection
        self.collection = self.db[collection_name]

    def get_all_documents(self):
        return list(self.collection.find())

    def collection_to_df(self):
        documents = self.get_all_documents()
        df = pd.DataFrame(documents)
        return df




