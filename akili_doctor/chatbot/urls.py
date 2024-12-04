from django.urls import path
from .views import ChatbotInteractionView

urlpatterns = [
    path("", ChatbotInteractionView.as_view(), name="chatbot-interaction"),
]