import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import os
import re
import time

nltk.download('vader_lexicon')


class Enricher:
    def __init__(self):
        self.sid = SentimentIntensityAnalyzer()
        base_dir = os.path.dirname(os.path.dirname(__file__))
        weapons_path = os.getenv("WEAPONS_FILE", os.path.join(base_dir, "data", "weapons.txt"))
        with open(weapons_path, "r") as f:
            self.weapons_list = [line.strip().lower() for line in f if line.strip()]

    def get_sentiment(self, text: str) -> str:
        """
        Use nltk sentiment analysis
        """
        scores = self.sid.polarity_scores(text)
        if scores["compound"] >= 0.05:
            return "positive"
        elif scores["compound"] <= -0.05:
            return "negative"
        else:
            return "neutral"

    def detect_weapons(self, text: str) -> list:
        """
        Find all weapon mentions in the text
        """
        text = text.lower()
        found = [weapon for weapon in self.weapons_list if weapon in text]
        return found

    @staticmethod
    def find_latest_date(text: str) -> str | None:
        """
        Find dates in the text that use
        format yyyy-mm-dd and get latest date
        """
        dates = re.findall(r"\b\d{4}-\d{2}-\d{2}\b", text)
        if not dates:
            return None
        return max(dates)

    def enrich(self, message: dict) -> dict:
        """
        Enrich message with sentiment,
        weapons, and latest date
        """
        text = message.get("text", "")
        date = message.get("CreateDate", "")
        return {
            **message,
            "sentiment": self.get_sentiment(text),
            "weapons": self.detect_weapons(text),
            "latest_date": self.find_latest_date(date),
            "enriched_at": time.strftime("%Y-%m-%d %H:%M:%S"),
        }

#validation only
if __name__ == "__main__":
    enricher = Enricher()

    msg = {"text": "Tomorrow we use a Rifle, a DRONE, and a missile!!!",
           "CreateDate": "2001-12-21 2022-10-01 2025-01-01"}
    e = Enricher()
    print(e.enrich(msg))