# Base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy and install dependencies from Retriever
COPY Retriever/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy all relevant folders
COPY Retriever /app/Retriever
COPY Kafka_Server /app/Kafka_Server
COPY Data /app/Data
COPY Data_Retrival /app/Data_Retrival
COPY Enricher /app/Enricher
COPY Mongo /app/Mongo
COPY Persister /app/Persister
COPY Preprocessor /app/Preprocessor
COPY Kafka_py /app/Kafka_py
COPY Scripts /app/Scripts

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV CONNECTION_STRING=""

# Set PYTHONPATH so imports across folders work
ENV PYTHONPATH="/app"

# Default command
CMD ["python", "Retriever/manager.py"]
