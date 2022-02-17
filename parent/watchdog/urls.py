# Imports
from django.urls import path

from watchdog.views import LoginView

# BEGIN

app_name = "watchdog"
urlpatterns = [
    path('login', LoginView.as_view(), name="login")
]

# END

if __name__ == '__main__':
    pass
