# Imports
from uuid import UUID
import logging
import os
import json

from smarttasks.models import STask


# BEGIN
logging.basicConfig(
    format="[%(levelname)s] %(name)s: %(msg)s",    
    level=logging.DEBUG
)

def master(id:UUID) -> None:
    # instantiate a logger
    log = logging.getLogger(f"smarttasks.master::{id.hex}")
    stask = STask.objects.get(sid=id)
    log.info(f"{stask.name} is run")

# END

if __name__ == '__main__':
    pass