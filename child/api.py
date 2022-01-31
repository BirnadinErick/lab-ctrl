import os
import json
import zipfile

from fastapi import FastAPI, Response, status

from contexts import RequestContext
from commands import shutdown
from utils import decrypt, encrypt

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
        # spawn aria2c and get the update file
        # TODO: Change to Popen
        try:
            os.system(f"aria2c.exe http://{mother}:2003/{up_file}")

            # spin new process and update
                # decode the update file
                # unzip the update file
            updates:list = []
            with zipfile.ZipFile(up_file, "r") as zip:
                updates = zip.namelist()
                zip.extractall()
                # update
                    # get list of updated files
                    # replace the new files for the old ones
                # run tests (if applicable)
            print(updates)
        except Exception as e:
            message = e.__str__()
        else:
            pass
        finally:
            payload, key = encrypt(message.join(f"\nID was: {id}"))
            return {"id" : key, "payload":payload}
    else:
        response.status_code = status.HTTP_304_NOT_MODIFIED
        return {"ver":version}
