# Imports
import json
from typing import Dict

from watchdog.models import Child

# BEGIN

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
def parse_instructions(sdata:str) -> str:

    # extract targets and steps
    try:
        sdata:Dict = json.loads(sdata)
        targets = [target.rstrip().lstrip() for target in sdata["targets"].split(",")]
        steps = sdata["steps"]
    except json.JSONDecodeError:
        raise Exception("sdata is invalid")

    # targets
    if "*" in targets:
        if len(targets) != 1:
            raise Exception("invalid targets value")
    else:
        # TODO: uncomment, commented for testing purposes
        # __validate_targets(targets)
        pass

    __validaet_steps(steps) # steps
    
    # after all the validations are checked, the user-input is safe to store
    return json.dumps({"steps": steps, "targets":targets})
# end parse_instructions ----------------------------------------------------------

# END

if __name__ == '__main__':
    pass