# Imports
from typing import Dict

from django.http import JsonResponse, HttpRequest

from error.utils import get_error_title
from error.models import Error
from watchdog.models import Child
from smarttasks.models import STask

# BEGIN

def get_unhandled_crictical_errors(req:HttpRequest, n:int):
    """
    Preprocess errors before injection
    and gets `n` unhandled errors

    Typical Return Value if `n` errors were found...
    {"es":[
            {
                "id": "192.168.1.51", 
                "title":"hey there"
            }
        ]
    }

    """
    errors:Dict = {} # define return object
    
    # get the neccessary errors
    errors_query = Error.objects.filter(isHandled=False, ecode__lt=2000, ecode__gt=1000)[:n]
    es_tmp:list = []
    for error in errors_query:
        e_tmp:dict
        victim:object
        # e_tmp["id"] = error.victim

        code = error.ecode
        # if ecode > 1500, then it belongs to the child
        if code > 1500 and code < 2000:
            victim = Child.objects.get(ip=error.victim).first()
            e_tmp["id"] = victim.nickname | victim.ip
        # if not then belongs to smart task
        elif code > 1000 and code < 1500:
            e_tmp["id"] = STask.objects.get(sid=error.victim).first().name
        # rarely error record may be corrupted
        else:
            raise Exception(f"Given ecode{error.ecode} in the error{error.eid} obj is invalid")

        e_tmp["title"] = get_error_title(error.ecode)

        es_tmp.append(e_tmp)
        del e_tmp, victim
    
    # compile the return object
    errors["es"] = es_tmp

    del es_tmp

    return JsonResponse(errors)

# END

if __name__ == '__main__':
    pass