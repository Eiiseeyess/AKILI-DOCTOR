from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import StreakSerializer

class StreakView(APIView):
    """Get the streak details for the authenticated user."""
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        streak_data = StreakSerializer(user).data
        return Response(streak_data)
