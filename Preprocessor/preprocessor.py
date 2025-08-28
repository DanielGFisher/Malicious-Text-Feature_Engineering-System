# Preprocessor/main.py
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from Kafka_Server.consumer import Consumer
from Kafka_Server.producer import Producer

nltk.download("stopwords")
nltk.download("wordnet")

class PreprocessingService:
    def __init__(self, topics=None):
        # initialize topics to listen to
        self.topics = topics or ["tweets_antisemitic", "tweets_not_antisemitic"]
        # Kafka consumer
        self.consumer = Consumer(topics=self.topics)
        # Kafka producer
        self.producer = Producer()
        # NLP tools
        self.stop_words = set(stopwords.words("english"))
        self.lemmatizer = WordNetLemmatizer()

    def clean_text(self, text: str):
        """
        Cleans text:
        - Removes punctuation and unique symbols
        - Converts to lowercase
        - Removes tabs, extra spaces, and stop words
        - Performs lemmatization
        """
        text = text.lower()
        text = re.sub(r"[^\w\s]", " ", text)
        text = re.sub(r"\s+", " ", text).strip()
        words = [w for w in text.split() if w not in self.stop_words]
        words = [self.lemmatizer.lemmatize(w) for w in words]
        return " ".join(words)

    def process_message(self, topic, message):
        """
        Process a single Kafka message
        """
        if not message or "original_text" not in message:
            return None

        processed_text = self.clean_text(message["original_text"])

        # add processed text as a new field
        message["clean_text"] = processed_text

        # determine target topic based on antisemitic field
        target_topic = (
            "preprocessed_tweets_antisemitic"
            if message.get("Antisemitic", 0) == 1
            else "preprocessed_tweets_not_antisemitic"
        )

        # publish to Kafka
        self.producer.send_message(target_topic, message)
        print(f"[LOG] Message processed from '{topic}' -> sent to '{target_topic}'")

    def run(self):
        """
        Run the Kafka preprocessing loop
        """
        print("- Preprocessor started, listening to Kafka -")
        for topic, message in self.consumer.get_message():
            self.process_message(topic, message)


if __name__ == "__main__":
    service = PreprocessingService()
    service.run()
