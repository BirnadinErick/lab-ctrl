from pydantic import BaseModel

class RequestContext(BaseModel):
    id: str
    payload: str

class ActionContext(BaseModel):
    code:int
    cron: str
    arg:str
