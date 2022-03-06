# Imports
import logging
import requests


# BEGIN

# begin shutdown_task --------------------------------------------------------
def shutdown(targets:list) -> bool:
    log = logging.getLogger("smarttasks.power_tasks::shutdown")
    log.info(f"Shutdown initiated on {targets}")
    return True
# end shutdown_task ----------------------------------------------------------

# END

if __name__ == '__main__':
    pass