# Imports
from typing import Any, Dict

from django.views.generic import TemplateView
from django.contrib.auth.models import User
from watchdog.utils import get_common_context_data

# BEGIN
class LoginView(TemplateView):
    template_name = "watchdog/auth/login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Login | Lab Ctrl"
        context["page_header"] = "Authenticate You"
        return context
    


# END

if __name__ == '__main__':
    pass