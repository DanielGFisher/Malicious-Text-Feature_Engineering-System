FROM python:3.11-slim

WORKDIR /app


COPY Retriever/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY Retriever/. /app/Retriever
COPY Kafka_Server/. /app/Kafka_Server


ENV PYTHONUNBUFFERED=1
ENV CONNECTION_STRING=""


CMD ["python","-m", "Retriever.manager"]


