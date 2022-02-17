# Imports
import subprocess as sp
from fastapi import FastAPI, Response, status, BackgroundTasks

from contexts import RequestContext, ActionContext
from utils import construct_response, deconstruct_request
from update import update_daemon
from commands import dispatch_action
from ACTIONS import *


# BEGIN

api:FastAPI = FastAPI()
version:float = 1.0
mother:str = "127.0.0.1"

@api.get("/", status_code=status.HTTP_302_FOUND)
async def root():
    """
    Mother will determine whether a node in the network is
    its child or not.
    """
    return construct_response({"msg": 1})


@api.post("/update", status_code=status.HTTP_202_ACCEPTED)
async def update(req:RequestContext, response:Response, backgroundTasks:BackgroundTasks):
    """
    Mother will post a payload like -
        {ver:version_number, up_file:update_catalog_name}
    to a child in its db and child will update itself if `ver` >= its `version`.
    If not, child returns 304 status immediately.
    """
    global version

    # decrypt the payload
    data = deconstruct_request(req)
    
    # check the version
    if data["ver"] > version:
        up_file = data["up_file"]

        # if update available, update
        backgroundTasks.add_task(update_daemon, src=up_file, address=f"http://{mother}:2003/")

        return construct_response({"msg": 1})
    else:
        response.status_code = status.HTTP_304_NOT_MODIFIED
        return construct_response({"msg":0, "ver":version})


@api.post("/act", status_code=status.HTTP_202_ACCEPTED)
async def act(req:RequestContext, res:Response, backgroundTasks:BackgroundTasks):
    """
    Endpoint for the mother to post the action, father
    wants the child to perform. Enqueues the action to be acted
    later and returns 202 status. If anything fails or otherwise,
    returns 406 status.
    """
    data:ActionContext = deconstruct_request(req)
    action_trigger = data["code"]
    if action_trigger == SHUTDOWN:
        backgroundTasks.add_task(dispatch_action, SHUTDOWN)
        return construct_response({"msg":1})
    elif action_trigger == LOGOFF:
        backgroundTasks.add_task(dispatch_action, LOGOFF)
        return construct_response({"msg":1})
    elif action_trigger == RESTART:
        backgroundTasks.add_task(dispatch_action, RESTART)
        return construct_response({"msg":1})
    elif action_trigger == EXEC_CMD:
        exec_cmd_out:sp.CompletedProcess = dispatch_action(EXEC_CMD)
        if exec_cmd_out.returncode != 0:
            return construct_response({"msg":exec_cmd_out.stderr.decode()})
        else:
            return construct_response({"msg":exec_cmd_out.stdout.decode()})
    elif action_trigger == EXEC_TASK:
        backgroundTasks.add_task(dispatch_action, EXEC_TASK)
        return construct_response({"msg":1})
    elif action_trigger == HEALTH_CHECK:
        health_stat_proc:sp.CompletedProcess = await dispatch_action(HEALTH_CHECK)
        return construct_response({"msg":health_stat_proc.stdout.decode()})
    else:
        res.status_code = status.HTTP_406_NOT_ACCEPTABLE
        return construct_response({"msg":0})

# END
