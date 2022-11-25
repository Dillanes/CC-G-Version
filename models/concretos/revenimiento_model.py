from pydantic import BaseModel, Field
from typing import Optional

class revendimiento_model(BaseModel):
    mm:int = Field(...)
    cm:int = Field(...)
    IN:str = Field(...,min_length=3,max_length=55)
    tipoConsistencia:str = Field(...,min_length=3,max_length=55)

    class Config:
        anystr_strip_whitespace = True