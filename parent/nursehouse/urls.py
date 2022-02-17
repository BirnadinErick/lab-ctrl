# Imports
from django.urls import path

from nursehouse.views import NurseHouseIndexView

# BEGIN

app_name = "nursehouse"
urlpatterns = [
    path('', NurseHouseIndexView.as_view(), name="index")
]

# END

if __name__ == '__main__':
    pass
