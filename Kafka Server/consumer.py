import json
from kafka import KafkaConsumer

class Consumer:
    def __init__(self, topics, bootstrap_servers="localhost:9092"):
        self.consumer = KafkaConsumer(
            *topics,
            bootstrap_servers=bootstrap_servers,
            auto_offset_reset="earliest",
            enable_auto_commit=True,
            group_id="preprocessor-group",
            value_deserializer=lambda v: json.loads(v.decode("utf-8"))
        )

    def get_message(self):
        for message in self.consumer:
            yield message.topic, message.value

    def close(self):
        self.consumer.close()
