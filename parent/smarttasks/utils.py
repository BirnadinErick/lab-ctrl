# Imports
import re
import json
from typing import Dict

from watchdog.models import Child
# BEGIN

# begin validate_cron --------------------------------------------------------
def __validate_cron(cron:str) -> list:
    """
        Validates given cron string whether it is supported by lab-ctrl or not
    """
    if len(re.findall("[a-zA-Z]|-|/|,", cron)):
        raise Exception("cron contains characters, which are not supported.")
    
    crons:list = [int(c) if (c != "*") else (c) for c in cron.split(" ")]
    
    if len(crons) != 5:
        raise Exception("cron contains too many/less options")
    
    if cron[0] < 0 or cron[0] > 59:
        raise Exception("cron minutes contains illegal values")

    if cron[1] < 0 or cron[1] > 23:
        raise Exception("cron hour contains illegal values")
    
    if cron[2] < 1 or cron[2] > 31:
        raise Exception("cron date contains illegal values")
    
    if cron[3] < 1 or cron[3] > 12:
        raise Exception("cron month contains illegal values")

    if cron[4] < 0 or cron[4] > 6:
        raise Exception("cron day contains illegal values")
    
    return crons
# end validate_cron ----------------------------------------------------------


# begin validate_targets ------------------------------------------------------
def __validate_targets(targets:list) -> None:
    
    children_ips = [c.ip for c in Child.objects.all()]

    for target in targets:
        if not(target in children_ips):
            raise Exception("a target specified is not found in the database")
# end validate_targets ----------------------------------------------------------


# begin validate_steps --------------------------------------------------------
def __validaet_steps(steps:list) -> None:
    try:
        for step in steps:
            # each checks
            if type(step) != int:
                raise
            
            if step == 0:
                raise
    except:
        raise Exception("wrong steps specified.")
# end validate_steps ----------------------------------------------------------

# begin parse_instructions --------------------------------------------------------
def parse_instructions(cron:str, sdata:str) -> str:

    # extract targets and steps
    try:
        sdata:Dict = json.loads(sdata)
        targets = [target.rstrip().lstrip() for target in sdata["targets"].split(",")]
        steps = sdata["steps"]
    except json.JSONDecodeError:
        raise Exception("sdata is invalid")

    # validations 
    crons:list = __validate_cron(cron) # cron
    
    # targets
    if "*" in targets and len(targets) > 1:
        raise Exception("invalid targets value")
    else:
        __validate_targets(targets)

    __validaet_steps(steps) # steps
    
    # after all the validations are checked, the user-input is safe to store
    instructions:Dict = {
        "cron": crons,
        "steps": steps
    }
    return json.dumps(instructions)
# end parse_instructions ----------------------------------------------------------

# END

if __name__ == '__main__':
    pass