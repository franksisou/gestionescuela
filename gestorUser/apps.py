from django.apps import AppConfig

class GestoruserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gestorUser'

    def ready(self):
        import gestorUser.signals
