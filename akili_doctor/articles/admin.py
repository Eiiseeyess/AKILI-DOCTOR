from django.contrib import admin
from .models import Article, UserArticlePreference

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'topic', 'is_trending', 'timestamp')

@admin.register(UserArticlePreference)
class UserArticlePreferenceAdmin(admin.ModelAdmin):
    list_display = ('user', 'preferred_topics')
