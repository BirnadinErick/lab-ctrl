# Imports
from django.views.generic import TemplateView

# BEGIN

class NurseHouseIndexView(TemplateView):
    template_name = "nursehouse/nursehouse.html"


# END

if __name__ == '__main__':
    pass
