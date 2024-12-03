from rest_framework import serializers
from Account.models import Account

class StreakSerializer(serializers.ModelSerializer):
    current_streak = serializers.IntegerField()
    longest_streak = serializers.IntegerField()

    class Meta:
        model = Account
        fields = ['current_streak', 'longest_streak']
