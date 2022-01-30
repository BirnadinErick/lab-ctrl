from fastapi import FastAPI

from child.contexts import RequestContext
from commands import shutdown

api = FastAPI()


@api.get("/")
async def root():
    return {"message": "Lab Ctrl is running"}

@api.post("/test")
async def test(req:RequestContext):
    print(req.payload)
    await shutdown()
    return {"res": "Test is Good"}

@api.post("/update")
async def update():
    
    # decrypt the payload
    # retrive the version
    # check the version
    # if update available
        # spawn aria2c and get the update file
        # spin new process and update
            # decode the update file
            # unzip the update file
            # update
                # get list of updated files
                # replace the new files for the old ones
            # run tests (if applicable)

        # return 201
    # else
        # return 200
    pass
