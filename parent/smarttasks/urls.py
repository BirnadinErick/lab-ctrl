# Imports
from django.urls import path

from smarttasks.views import SmartTasksIndexView

# BEGIN

app_name = "smarttasks"
urlpatterns = [
    path('', SmartTasksIndexView.as_view(), name="index")

]

# END

if __name__ == '__main__':
    pass
