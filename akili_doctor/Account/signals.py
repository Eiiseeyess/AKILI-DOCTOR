from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Account

@receiver(post_save, sender=Account)
def generate_jwt_token(sender, instance=None, created=False, **kwargs):
    if created:
        refresh = RefreshToken.for_user(instance)
        print(f"Access Token: {str(refresh.access_token)}")
        print(f"Refresh Token: {str(refresh)}")
