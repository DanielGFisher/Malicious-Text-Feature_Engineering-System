from Kafka_Server.consumer import Consumer
from Kafka_Server.producer import Producer
from preprocessor import Preprocessor

def run_service():
    consumer = Consumer(
        topics=["raw_tweets_antisemitic", "raw_tweets_not_antisemitic"]
    )
    producer = Producer()
    preprocessor = Preprocessor()

    print("- Preprocessor started, listening to kafka -")

    for topic, message in consumer.get_message():
        text = message.get("text", "")
        processed_text = preprocessor.clean_text(text)

        enriched_message = {
            "original_message": message,
            "preprocessed_message": processed_text,
        }

        if topic == "raw_tweets_antisemitic":
            target = "preprocessed_tweets_antisemitic"
        else:
            target = "preprocessed_tweets_not_antisemitic"

        producer.send_message(target, enriched_message)

if __name__ == "__main__":
    run_service()
