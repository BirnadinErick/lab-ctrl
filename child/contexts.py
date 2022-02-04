from pydantic import BaseModel

class RequestContext(BaseModel):
    id: bytes
    payload: bytes
