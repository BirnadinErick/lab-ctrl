# Imports
from django.views.generic import TemplateView

# BEGIN

class SmartTasksIndexView(TemplateView):
    template_name = "smarttasks/smarttasks.html"


# END

if __name__ == '__main__':
    pass