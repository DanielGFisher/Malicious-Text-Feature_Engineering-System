from pymongo import MongoClient


class Persister:
    def __init__(self, db_name="antisemitic_tweets"):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client[db_name]
        self.antisemitic_collection = self.db["tweets_antisemitic"]
        self.not_antisemitic_collection = self.db["tweets_not_antisemitic"]

    def save_tweet(self, tweet: dict):
        """
        tweet: {
            "createdate": datetime,
            "antisemitic": 0/1,
            "original_text": str,
            "clean_text": str,
            "sentiment": str,
            "weapons_detected": list,
            "relevant_timestamp": str
        }
        """
        antisemitic_flag = bool(tweet.get("antisemitic", 0))

        if antisemitic_flag:
            self.antisemitic_collection.insert_one(tweet)
        else:
            self.not_antisemitic_collection.insert_one(tweet)
