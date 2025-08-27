import time
from connection_db import ConnectionDB
f


class Manager:

    def __init__(self):

        self.db = ConnectionDB()
        self.producer = Producer()

    def run(self):
        while True:
            try:
                data = self.db.get_data_batch()
                for dic in data:
                    if dic.get("Antisemitic") == 1:
                        self.producer.send_data(dic, "tweets_antisemitic")
                    else:
                        self.producer.send_data(dic, "tweets_not_antisemitic")
                print(f"Sent {len(data)} docs to Kafka")

            except Exception as e:
                print(f"Error during processing: {e}")

            time.sleep(60)


if __name__ == "__main__":
    manager = Manager()
    manager.run()
