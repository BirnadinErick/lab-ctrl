# Imports
import json
from typing import Dict

from django.http import JsonResponse, HttpRequest, HttpResponseNotAllowed, HttpResponseServerError
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt

from watchdog.utils import get_common_context_data
from smarttasks.models import STask
# BEGIN

class SmartTasksIndexView(TemplateView):
    template_name = "smarttasks/smarttasks.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return {
            **context, 
            **get_common_context_data(title="SMART TASKS | Aden", page_header="Smart Tasks in Aden")
        }
    

# begin add new stask --------------------------------------------------------
@csrf_exempt
def add_smart_task(req:HttpRequest) -> JsonResponse:
    # prologue
    if req.method == "POST":
        data:Dict = json.loads(req.body)
    else:
        return HttpResponseNotAllowed(["POST"])

    # core
    try:
        # create new STask
        stask_new = STask(
            name=data["name"],
            instructions=data["data"]
        )
        # commit it
        stask_new.save()

        # schedule it accordingly

    except Exception as e:
        return HttpResponseServerError()
    else:
        return JsonResponse({"msg":"1"})

# end add new stask ----------------------------------------------------------

# END

if __name__ == '__main__':
    pass