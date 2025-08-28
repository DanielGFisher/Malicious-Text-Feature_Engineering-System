from Kafka_Server.consumer import Consumer
from Kafka_Server.producer import Producer
from Enricher.enricher import Enricher


class EnricherService:
    def __init__(self, topics=None):
        self.topics = topics or [
            "preprocessed_tweets_antisemitic",
            "preprocessed_tweets_not_antisemitic"
        ]
        self.consumer = Consumer(topics=self.topics)
        self.producer = Producer()
        self.enricher = Enricher()
        self.topic_mapping = {
            "preprocessed_tweets_antisemitic": "enriched_preprocessed_tweets_antisemitic",
            "preprocessed_tweets_not_antisemitic": "enriched_preprocessed_tweets_not_antisemitic"
        }

    def process_message(self, topic, message):
        """
        Enrich a single Kafka message
        """
        if not message or "text" not in message:
            return None

        enriched_message = self.enricher.enrich(message)
        target_topic = self.topic_mapping.get(topic, f"enriched_{topic}")
        self.producer.send_message(target_topic, enriched_message)

        print(f"[LOG] Message enriched from '{topic}' -> sent to '{target_topic}'")

    def run(self):
        """
        Run Kafka consumer loop
        """
        print("- Enricher service started, listening to Kafka -")
        for topic, message in self.consumer.get_message():
            self.process_message(topic, message)


if __name__ == "__main__":
    service = EnricherService()
    service.run()
