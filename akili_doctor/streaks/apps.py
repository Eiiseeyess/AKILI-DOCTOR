from django.apps import AppConfig


class StreaksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'streaks'

    def ready(self):
        '''Import the signals appropriately when the app is ready'''
        import streaks.signals