from django.db import models
from Account.models import Account
from django.conf import settings

class Article(models.Model):
    TOPIC_CHOICES = [
    ('Anxiety', 'Anxiety'),
    ('Depression', 'Depression'),
    ('Stress', 'Stress'),
    ('Wellness', 'Wellness'),
    ('Self-Esteem', 'Self-Esteem'),
    ('Mindfulness', 'Mindfulness'),
    ('Burnout', 'Burnout'),
    ('Trauma', 'Trauma'),
    ('Grief', 'Grief'),
    ('Relationships', 'Relationships'),
    ('Addiction', 'Addiction'),
    ('Sleep Health', 'Sleep Health'),
    ('Work-Life Balance', 'Work-Life Balance'),
    ('Emotional Regulation', 'Emotional Regulation'),
    ('Body Image', 'Body Image'),
    ('Coping Strategies', 'Coping Strategies'),
    ('Parenting', 'Parenting'),
    ('PTSD', 'PTSD'),
    ('ADHD', 'ADHD'),
    ('Eating Disorders', 'Eating Disorders'),
    ]

    title = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True)  
    link = models.URLField(null=True, blank=True)  
    topic = models.CharField(max_length=50, choices=TOPIC_CHOICES)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_trending = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class UserArticlePreference(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='article_preferences', 
    )
    preferred_topics = models.JSONField(default=list)
    read_articles = models.ManyToManyField(Article, blank=True, related_name='read_by')

    def __str__(self):
        return f"{self.user.username}'s Preferences"
