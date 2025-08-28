# Iranian Tweet Processing Pipeline

## Introduction:
Hi! This project is our implementation of a Kafka-based ETL pipeline.  
The goal is to take tweet-like messages from a MongoDB Atlas database, process them step by step, enrich them with extra features, save them into a local database, and finally make them accessible through a small REST API.  

Think of it as:  
Raw Data → Kafka → Clean → Enrich → Save → Query with API

---

## What We Built

### 1. Retriever:
- Connects to MongoDB Atlas.
- Every minute it pulls the 100 oldest records.
- Publishes them to Kafka:
  - `raw_tweets_antisemitic`
  - `raw_tweets_not_antisemitic`

---

### 2. Preprocessor:
- Listens to the raw Kafka topics.
- Cleans the text:
  - removes punctuation, weird characters, stopwords, extra spaces
  - lowercases everything
  - lemmatization
- Adds a new field called `clean_text`.
- Publishes to:
  - `preprocessed_tweets_antisemitic`
  - `preprocessed_tweets_not_antisemitic`

---

### 3. Enricher:
- Listens to preprocessed data.
- Adds more meaning to the tweets:
  - Sentiment: positive, negative, neutral
  - Weapons detected: finds weapon names from a blacklist
  - Relevant timestamp: if a date is written in the text, take the latest one
- Publishes to:
  - `enriched_preprocessed_tweets_antisemitic`
  - `enriched_preprocessed_tweets_not_antisemitic`

---

### 4. Persister:
- Subscribes to enriched Kafka topics.
- Saves the final version into local MongoDB:
  - `tweets_antisemitic`
  - `tweets_not_antisemitic`

Final documents look like this:
```json
{
  "id": "64fcf0d2a1b23c0012345678",
  "createdate": "2020-03-24T09:28:15.000+00:00",
  "antisemitic": 0,
  "original_text": "Tomorrow (25/03/2020 09:30) we will attack using a gun (AK-47) near the border",
  "clean_text": "tomorrow attack use gun ak-47 near border",
  "sentiment": "negative",
  "weapons_detected": ["gun", "AK-47"],
  "relevant_timestamp": "25/03/2020"
}
