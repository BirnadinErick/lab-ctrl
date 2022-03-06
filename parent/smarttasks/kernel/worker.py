# Imports
from typing import Dict
from uuid import UUID
import logging
import json
import asyncio

from smarttasks.models import STask
from smarttasks.kernel.power_tasks import *
from watchdog.models import Child

# BEGIN

# all the tasks
TASKS:Dict = {
    1: shutdown
}

# begin master --------------------------------------------------------
def master(id:UUID) -> None:
    log = logging.getLogger(f"smarttasks.master::{id.hex}")

    try:
        stask:STask = STask.objects.get(sid=id)
    except Exception as e:
        log.error(e.__str__())
    
    instructions:Dict = json.loads(stask.instructions)
    targets, steps = instructions["targets"], instructions["steps"]

    if targets[0] == "*":
        targets = [c.ip for c in Child.objects.all()]

    for step in steps:
        log.info(f"Running step {step}")
        asyncio.run(TASKS[step](targets))

# end master ----------------------------------------------------------
    

# END

if __name__ == '__main__':
    pass