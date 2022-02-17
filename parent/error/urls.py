# Imports
from django.urls import path

from error.views import get_unhandled_crictical_errors

# BEGIN

app_name = "error"
urlpatterns = [
    path('get/<int:n>', get_unhandled_crictical_errors, name="get_cric_unh_es")
]

# END

if __name__ == '__main__':
    pass
