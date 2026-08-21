# Step 1: Use an official lightweight Python image
FROM python:3.11-slim

# Step 2: Set the directory inside the container where code will live
WORKDIR /app

# Step 3: Copy the requirements file and install dependencies
COPY myproject/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Step 4: Pre-download the Hugging Face model *inside* the container image.
# This prevents the container from downloading the model every time it restarts!
RUN python -c "from transformers import pipeline; pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')"

# Step 5: Copy the rest of your project files into the container
COPY . .

# Step 6: Expose the port that Django will run on
EXPOSE 8000

# Step 7: Command to run the production server
CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:8000"]

