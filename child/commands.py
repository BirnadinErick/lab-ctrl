# Imports
import sys
import subprocess as sp
import os


# BEGIN

# global vars
cwd:str = os.getcwd()
dispatcher_bin:str = "dispatcher.exe"


async def dispatch_action(action:int) -> sp.CompletedProcess | None:
    # use Popen if version of py interpreter < 3.5
    
    if sys.version_info.major < 3 and sys.version_info.minor < 5: 
        sp.Popen(
                args=f"{dispatcher_bin} {action}",
                cwd=cwd
        )
    else:

        dispatched:sp.CompletedProcess = sp.run(
                                                args=f"{dispatcher_bin} {action}",
                                                capture_output=True
                                            )
        return dispatched

# END

if __name__ == '__main__':
    pass