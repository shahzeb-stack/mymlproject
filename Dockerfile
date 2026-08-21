FROM python:3.11-slim
WORKDIR /app

# FIX: Copy the file directly from the root main directory
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Pre-download the Hugging Face model weights inside the container image cache layer
RUN python -c "from transformers import pipeline; pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')"

COPY . .
EXPOSE 8000
CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:8000"]
