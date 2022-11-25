from pydantic import BaseModel,Field
from typing import Optional

class fibra_model(BaseModel):
    tipoFibraMaterial:str = Field(...,min_length=3,max_length=55)
    fibraConcreto:str = Field(...,min_length=3,max_length=55)
    tipoFibra:str = Field(...,min_length=3, max_length=55)

    class Config:
        anystr_strip_whitespace = True

