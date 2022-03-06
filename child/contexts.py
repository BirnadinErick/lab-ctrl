from pydantic import BaseModel

class RequestContext(BaseModel):
    id: bytes | str
    payload: bytes | str

class ActionContext(BaseModel):
    code:int
    cron: str
    arg:str
