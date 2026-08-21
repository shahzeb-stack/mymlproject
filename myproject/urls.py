from django.contrib import admin
from django.urls import path
from .views import predict_sentiment

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/predict/', predict_sentiment, name='predict'),
]
