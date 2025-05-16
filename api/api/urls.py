from django.urls import path
from app.views import analyze_security

urlpatterns = [
    path('analyze/', analyze_security),
]