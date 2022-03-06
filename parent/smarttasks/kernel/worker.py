# Imports
from typing import Dict
from uuid import UUID
import logging
import json

from smarttasks.models import STask
from smarttasks.kernel.power_tasks import *

# BEGIN

# all the tasks
TASKS:Dict = {
    1: shutdown
}

# begin master --------------------------------------------------------
def master(id:UUID) -> None:
    # instantiate a logger
    log = logging.getLogger(f"smarttasks.master::{id.hex}")
    # get the stask
    try:
        stask:STask = STask.objects.get(sid=id)
    except Exception as e:
        log.error(e.__str__())
    
    instructions:Dict = json.loads(stask.instructions)
    targets, steps = instructions["targets"], instructions["steps"]

    for step in steps:
        log.info(f"Running step {step}")
        status:bool = TASKS[step](targets)
        if status:
            log.debug(f"Step {step} returned success code")
            continue
        else:
            log.error(f"Step {step} returned error code")
# end master ----------------------------------------------------------
    

# END

if __name__ == '__main__':
    pass