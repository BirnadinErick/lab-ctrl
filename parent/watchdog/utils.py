# Imports
from typing import Any, Dict

# from django.contrib.auth.models import User
from django.conf import settings


# BEGIN


# begin universal template env vars --------------------------------------------------------
def get_common_context_data(request:Any=None):
    common_context:Dict[str, Any] = dict()
    # common_context["appuser"] = request.user
    common_context["mother"] = settings.MOTHER_URI
    return common_context
# end universal template env vars ----------------------------------------------------------


# END

if __name__ == '__main__':
    raise Exception(f"{__file__} not to be used as a standalone script!")