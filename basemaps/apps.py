# basemaps/apps.py
from django.apps import AppConfig

class BasemapsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'basemaps'
    verbose_name = 'Basemaps'