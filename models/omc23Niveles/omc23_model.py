from pydantic import BaseModel,Field
from typing import Optional


class omc23_model(BaseModel):
    omniclass: str = Field(...)
    descripcion:str = Field(...)
    level:str = Field(...)
    L1:str = Optional[str]
    L2:str = Optional[str]
    L3:str = Optional[str]
    L4:str = Optional[str]
    L5:str = Optional[str]
    L6:str = Optional[str]
    L7:str = Optional[str]
    CodigoOmniclass:str = Field(...)


    class Config:
        anystr_strip_whitespace = True


