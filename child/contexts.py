from pydantic import BaseModel

class RequestContext(BaseModel):
    id: bytes
    payload: bytes

class ActionContext(BaseModel):
    code:int
    cron: str
    arg:str
