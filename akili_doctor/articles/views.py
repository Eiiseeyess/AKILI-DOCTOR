from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status
from .models import Article, UserArticlePreference
from .serializers import ArticleSerializer, UserArticlePreferenceSerializer
from .permissions import IsAuthor

class ArticleListCreateView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]

class ArticleListView(generics.ListAPIView):
    """List articles filtered by user preferences."""
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]
    queryset = Article.objects.all()

class TrendingArticlesView(generics.ListAPIView):
    """List trending articles."""
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Article.objects.filter(is_trending=True).order_by('-timestamp')

class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Get, update, or delete an article by ID, only if the user is the author."""
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated, IsAuthor]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class UpdateUserPreferencesView(APIView):
    """Update user preferences for topics."""
    permission_classes = [IsAuthenticated]

    def post(self, request):
        preferences = request.data.get('preferred_topics', [])
        if not isinstance(preferences, list):
            return Response({"error": "Preferred topics must be a list."}, status=status.HTTP_400_BAD_REQUEST)
        
        user_pref, _ = UserArticlePreference.objects.get_or_create(user=request.user)
        user_pref.preferred_topics = preferences
        user_pref.save()
        return Response({"detail": "Preferences updated successfully."}, status=status.HTTP_200_OK)
