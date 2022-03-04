# Imports
import random
from datetime import datetime as dt

from django.views.generic import TemplateView
from django.http import JsonResponse
from django.conf import settings

from watchdog.models import Child
from watchdog.utils import get_common_context_data
from watchdog.metadata.metadata_managers import manage_children_metadata
from watchdog.metadata.actions_index import GET_CHILDREN_METADATA
# BEGIN

# dummy mock-api response
mother_res:dict = {
    "healthy_children": 12,
    "total_children": 34,
}

class DashboardView(TemplateView):
    template_name = "dashboard/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["es_n"] = settings.ERROR_DASHBOARD_COUNT
        context["title"] = "Dashboard | Lab Ctrl"
        context["page_header"] = "Dashboard of Aden" # aqquire family name and display
        context["children"] = Child.objects.all().order_by('nickname', 'ip')
        
        return {
            **get_common_context_data(), 
            **context,
            **manage_children_metadata(GET_CHILDREN_METADATA)
        }


# begin api methods for graph plotting --------------------------------------------------------
def meandata(req):
    """
        Send Mean Load data.

        returns json of:-
            {[{
                name: "CPU %",
                data: [load data of last 2 weeks]
            },{
                {
                name: "Memory %",
                data: [load data of last 2 weeks]
            }]}
    """
    response = {
        "cpu":{
            "name":"CPU %",
            "data": [round(random.random()*100, 2) for i in range(12)]
        },
        "mem":{
            "name":"Memory %",
            "data": [round(random.random()*100, 2) for i in range(12)]
        },
        "cat":{
            "categories": [
                f"{random.randint(1,31)}/{i}"
                for i in range(12)
            ]
        }
    }
    return JsonResponse(response)
# end api methods for graph plotting ----------------------------------------------------------
    


# END

if __name__ == '__main__':
    pass