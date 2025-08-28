import time
from connection_db import ConnectionDB
from Kafka_Server.producer import Producer
from bson.json_util import dumps, loads

class Manager:

    def __init__(self):
        self.db = ConnectionDB()
        self.producer = Producer()

    def run(self):
        page = 0
        while True:
            try:
                data = self.db.get_data_batch(page=page)
                for dic in data:

                    if "_id" in dic:
                        dic["_id"] = str(dic["_id"])

                    if "CreateDate" in dic:
                        dic["CreateDate"] = dic["CreateDate"].isoformat()

                    if dic.get("Antisemitic") == 1:
                        self.producer.send_message("tweets_antisemitic",dic)
                    else:
                        self.producer.send_message("tweets_not_antisemitic",dic)

                print(f"Sent {len(data)} docs to Kafka")
                page += 1

            except Exception as e:
                print(f"Error during processing: {e}")

            time.sleep(60)


if __name__ == "__main__":
    manager = Manager()
    manager.run()
