from Kafka_Server.consumer import Consumer
from Kafka_Server.producer import Producer
from preprocessor import Preprocessor


class PreprocessingService:
    def __init__(self, topics=None):
        self.topics = topics or ["tweets_antisemitic", "tweets_not_antisemitic"]
        self.consumer = Consumer(topics=self.topics)
        self.producer = Producer()
        self.preprocessor = Preprocessor()

    def process_message(self, topic, message):
        """Process a single Kafka message."""
        if not message or "text" not in message:
            return None

        text = message.get("text", "")
        processed_text = self.preprocessor.clean_text(text)

        enriched_message = {
            "original_message": message,
            "preprocessed_message": processed_text,
        }

        target = f"preprocessed_{topic}"
        self.producer.send_message(target, enriched_message)

        print(f"[LOG] Message processed from '{topic}' -> sent to '{target}'")

    def run(self):
        """Run the Kafka preprocessing loop."""
        print("- Preprocessor started, listening to kafka -")

        for topic, message in self.consumer.get_message():
            self.process_message(topic, message)


if __name__ == "__main__":
    service = PreprocessingService()
    service.run()
