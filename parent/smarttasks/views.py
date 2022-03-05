# Imports
from django.views.generic import TemplateView

from watchdog.utils import get_common_context_data
# BEGIN

class SmartTasksIndexView(TemplateView):
    template_name = "smarttasks/smarttasks.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return {
            **context, 
            **get_common_context_data(title="SMART TASKS | Aden", page_header="Smart Tasks in Aden")
        }
    


# END

if __name__ == '__main__':
    pass