FROM python:3.11-slim


ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    NLTK_DATA=/usr/local/share/nltk_data



WORKDIR /app


COPY Preprocessor/requirements.txt Preprocessor/requirements.txt
RUN pip install --no-cache-dir -r Preprocessor/requirements.txt


COPY . .


RUN python - 'PY'\nimport nltk; nltk.download('wordnet'); nltk.download('omw-1.4'); nltk.download('stopwords')\nPY


CMD ["python", "-m", "Preprocessor.main"]
