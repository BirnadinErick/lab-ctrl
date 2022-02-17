# Imports
from django.urls import path

from dashboard.views import DashboardView, meandata

# BEGIN

app_name = "dashboard"
urlpatterns = [
    path('', DashboardView.as_view(), name="index"),
    path('meandata', meandata, name="meandata"),

]

# END

if __name__ == '__main__':
    pass
