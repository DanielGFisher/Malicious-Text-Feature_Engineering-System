FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY . /app/Retriever

ENV PYTHONUNBUFFERED=1
ENV CONNECTION_STRING=""

CMD ["python", "Retriever/manager.py"]

