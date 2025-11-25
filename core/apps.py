from django.apps import AppConfig

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        # Ejecutar el script para crear un superusuario automáticamente
        import core.create_superuser
