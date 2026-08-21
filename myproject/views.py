import os
import mlflow
from django.http import JsonResponse
from rest_framework.decorators import api_view
from transformers import pipeline
from dotenv import load_dotenv

# Load environment variables from a hidden file
load_dotenv()

# Configure MLflow to log to our remote dashboard online
mlflow.set_tracking_uri(os.getenv("MLFLOW_TRACKING_URI", ""))

# Initialize Hugging Face pipeline (downloads a small text analyzer model)
classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

@api_view(['POST'])
def predict_sentiment(request):
    text = request.data.get('text', '')
    if not text:
        return JsonResponse({'error': 'No text provided'}, status=400)
    
    # Run the Hugging Face model prediction
    result = classifier(text)[0]
    
    # MLOps Tracking: Log details to MLflow online
    try:
        with mlflow.start_run(run_name="production_inference"):
            mlflow.log_param("text_length", len(text))
            mlflow.log_metric("confidence_score", result['score'])
            mlflow.log_param("predicted_sentiment", result['label'])
    except Exception as e:
        print(f"MLflow Logging Failed: {e}") 

    # Return the response to the user
    return JsonResponse({
        'text': text, 
        'label': result['label'], 
        'score': result['score']
    })

