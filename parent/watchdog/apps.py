# Imports
import logging

from django.conf import settings
from django.apps import AppConfig

# BEGIN
class WatchdogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'watchdog'

    def ready(self) -> None:
        logging.basicConfig(
            format=settings.LOGGER_FORMAT,
            level=settings.LOGGER_LEVEL
        )
        return super().ready()

# END

if __name__ == '__main__':
    pass