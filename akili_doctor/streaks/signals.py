from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from Account.models import Account

@receiver(post_save, sender=Account)
def update_streak_on_login(sender, instance, **kwargs):
    """Track login streaks and update accordingly"""
    if instance.last_login:
        last_login_date = instance.last_login.date()
        today = timezone.now().date()

        if last_login_date == today - timezone.timedelta(days=1):
            instance.current_streak += 1
        else:
            instance.current_streak = 1 
        
        if instance.current_streak > instance.longest_streak:
            instance.longest_streak = instance.current_streak

        instance.last_login_date = today
        instance.save()

