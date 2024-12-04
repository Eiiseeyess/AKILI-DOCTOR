from django.urls import path
from .views import ArticleListCreateView ,ArticleListView, TrendingArticlesView, UpdateUserPreferencesView, ArticleDetailView

urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('post/', ArticleListCreateView.as_view(), name='article-creation'),
    path('trending/', TrendingArticlesView.as_view(), name='trending-articles'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('preferences/', UpdateUserPreferencesView.as_view(), name='update-preferences'),
]
