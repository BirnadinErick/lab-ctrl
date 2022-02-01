# Imports
import os
import json
import zipfile
import subprocess

from fastapi import FastAPI, Response, status

from contexts import RequestContext
from commands import shutdown
from utils import decrypt, encrypt, update_daemon


# BEGIN

api:FastAPI = FastAPI()
version:float = 1.0
mother:str = "127.0.0.1"

@api.get("/")
async def root():
    return {"message": "Lab Ctrl is running"}

@api.post("/update", status_code=status.HTTP_202_ACCEPTED)
async def update(req:RequestContext, response:Response):
    message:str = str()
    id:bytes = req.id
    
    # decrypt the payload
    payload = decrypt(req.payload, req.id)
    
    # retrive the version
    data = json.loads(payload.decode())
    del payload

    # check the version
    if data["ver"] > version:
        up_file = data["up_file"]
        del data    # clear the data sice we don't need it anymore

    # if update available
        if not update_daemon(up_file, f"http://{mother}:2003/"):
            data = {"msg":"update_failed"}    
        else:
            data = {"msg":"update_ok"}
        
        jData = json.dumps(data)
        enc_data, key = encrypt(jData)

        return {"id":key, "payload":enc_data}
    else:
        response.status_code = status.HTTP_304_NOT_MODIFIED
        return {"ver":version}

# END

if __name__ != '__main__':
    raise Exception("Not to be used as a module, but as a standalone(partial) script")