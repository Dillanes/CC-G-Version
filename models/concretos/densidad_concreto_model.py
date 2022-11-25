from pydantic import BaseModel,Field
from typing import Optional

class densidad_concreto_model(BaseModel):
    tipoConcreto:str = Field(...,min_length=3, max_length=55)
    kgm3:int = Field(...)
    lbft3:float =  Field(...)

    class Config:
        anystr_strip_whitespace= True


