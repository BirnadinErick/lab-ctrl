# Imports
from django.contrib import admin
from django.urls import path, include

# BEGIN

urlpatterns = [
    path('admin/', admin.site.urls),
    path('watchdog/', include('watchdog.urls')),
    path('', include('dashboard.urls')),
    path('smarttasks/', include('smarttasks.urls')),
    path('nursehouse/', include('nursehouse.urls')),
    path('error/', include('error.urls')),
]


# END

if __name__ == '__main__':
    pass