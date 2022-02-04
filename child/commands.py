import subprocess as sp
import os

cwd:str = os.getcwd()

async def shutdown():
    sp.Popen(
        args="dispatcher.exe",
        cwd=cwd
    )
