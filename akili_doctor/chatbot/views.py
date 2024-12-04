from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .services import get_rasa_response

class ChatbotInteractionView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user_message = request.data.get("message")
        if not user_message:
            return Response({"error": "Message is required for Faraja to understand and respond to your mental and cognitive being."}, status=400)
        bot_response = get_rasa_response(user_message, sender_id=request.user.username)
        return Response({"bot_response": bot_response})
