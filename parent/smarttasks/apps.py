# Imports
from django.apps import AppConfig

from smarttasks.task_workers.scheduler import scheduler

# BEGIN

class SmarttasksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'smarttasks'

    def ready(self) -> None:
        # start the scheduler
        scheduler.start()
        return super().ready()


# END

if __name__ == '__main__':
    pass