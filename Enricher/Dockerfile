FROM python:3.11-slim


ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app


COPY Enricher/requirements.txt Enricher/requirements.txt
RUN pip install --no-cache-dir -r Enricher/requirements.txt


COPY . .


CMD ["python", "-m", "Enricher.main"]
