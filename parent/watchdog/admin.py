# Imports
from django.contrib import admin

from watchdog.models import Child, STask_Child, AppUser


# BEGIN

admin.site.register(Child)
admin.site.register(STask_Child)
admin.site.register(AppUser)


# END

if __name__ == '__main__':
    pass