# Imports
import json

from fastapi import FastAPI, Response, status, BackgroundTasks

from contexts import RequestContext
from commands import shutdown
from utils import decrypt, encrypt
from update import update_daemon


# BEGIN

api:FastAPI = FastAPI()
version:float = 1.0
mother:str = "127.0.0.1"

@api.get("/")
async def root():
    return {"message": "Lab Ctrl is running"}

@api.post("/update", status_code=status.HTTP_202_ACCEPTED)
async def update(req:RequestContext, response:Response, bgTasks:BackgroundTasks):
    global version

    # decrypt the payload
    payload = decrypt(req.payload, req.id)
    
    # retrive the version
    data = json.loads(payload.decode())
    del payload

    # check the version
    if data["ver"] > version:
        up_file = data["up_file"]

        # if update available, update
        bgTasks.add_task(update_daemon, src=up_file, address=f"http://{mother}:2003/")

        data = {"msg": "Updated added to background tasks!"}
        jData = json.dumps(data)
        enc_data, key = encrypt(jData)

        return {"id":key, "payload":enc_data}
    else:
        response.status_code = status.HTTP_304_NOT_MODIFIED
        return {"ver":version}

# END
