from pydantic import BaseModel,Field
from typing import Optional


class clase_exposicion_model(BaseModel):
    minimaAC:float = Field(...)
    minimaAFC:str = Field(...,min_length=3,max_length=45)
    categoria:str = Field(...,min_length=3,max_length=45)
    clase:str = Field(...,min_length=3,max_length=45)
    condicion:str = Field(...,min_length=3,max_length=45)


    class Config:
        anystr_strip_whitespace = True