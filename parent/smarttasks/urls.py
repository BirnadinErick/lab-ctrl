# Imports
from django.urls import path

from smarttasks.views import SmartTasksIndexView, add_smart_task

# BEGIN

app_name = "smarttasks"
urlpatterns = [
    path('', SmartTasksIndexView.as_view(), name="index"),
    path('new', add_smart_task, name="new")

]

# END

if __name__ == '__main__':
    pass
