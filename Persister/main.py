from Kafka_Server.consumer import Consumer
from Persister.persister import Persister
from datetime import datetime


class PersistenceService:
    def __init__(self, topics=None):
        self.topics = topics or [
            "enriched_preprocessed_tweets_antisemitic",
            "enriched_preprocessed_tweets_not_antisemitic"
        ]
        self.consumer = Consumer(topics=self.topics)
        self.persister = Persister()

    def process_message(self, topic, message):
        """
        Save a single Kafka message to MongoDB
        """
        if not message:
            return

        createdate_str = message.get("createdate")
        if createdate_str:
            try:
                message["createdate"] = datetime.fromisoformat(createdate_str)
            except Exception:
                message["createdate"] = datetime.utcnow()
        else:
            message["createdate"] = datetime.utcnow()

        if "latest_date" in message:
            message["relevant_timestamp"] = message.pop("latest_date")
        if "weapons" in message:
            message["weapons_detected"] = message.pop("weapons")

        self.persister.save_tweet(message)
        print(f"[LOG] Saved tweet ID {message.get('id')} from topic '{topic}'")

    def run(self):
        """
        Run the persistence loop
        """
        print("- Persistence Service started, listening to Kafka -")
        for topic, message in self.consumer.get_message():
            self.process_message(topic, message)

    def shutdown(self):
        """
        Close Kafka and MongoDB connections
        """
        self.consumer.close()
        self.persister.client.close()
        print("Connections closed.")


if __name__ == "__main__":
    service = PersistenceService()
    service.run()
