from kafka import KafkaProducer
import json

class Producer:
    def __init__(self, broker='localhost:9092'):#host.docker.internal:9092
        self.producer = KafkaProducer(
            bootstrap_servers=broker,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )

    def send_message(self, topic, message: dict):
        self.producer.send(topic, message)
        self.producer.flush()

    def close(self):
        self.producer.close()