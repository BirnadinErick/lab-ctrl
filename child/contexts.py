from uuid import UUID
from typing import Union
from pydantic import BaseModel

class RequestContext(BaseModel):
    id: bytes
    payload: bytes
