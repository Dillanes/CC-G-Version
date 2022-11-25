from pydantic import BaseModel,Field
from typing import Optional

class edad_resistencia_model(BaseModel):
    dias:int = Field(...)
    descripcion:str = Field(...,min_length=3,max_length=255)

    class Config:
        anystr_strip_whitespace = True