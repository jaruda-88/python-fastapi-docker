from pydantic import BaseModel
from typing import Optional, List

class Res(BaseModel):
    name: str


class TestCreate(BaseModel):
    id: int 
    name: str

    class Config:
        orm_mode = True
