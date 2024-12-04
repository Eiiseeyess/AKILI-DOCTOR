from rest_framework import serializers
from .models import Article, UserArticlePreference
from django.conf import settings

class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    author_username = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Article
        fields = ['id', 'title', 'author', 'author_username', 'content', 'link', 'topic', 'is_trending', 'timestamp']

class UserArticlePreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserArticlePreference
        fields = ['user', 'preferred_topics', 'read_articles']
        extra_kwargs = {'user': {'read_only': True}}
