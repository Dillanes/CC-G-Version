from pydantic import BaseModel,Field
from typing import Optional


class resistencia_concreto_model(BaseModel):
    kgcm2:int = Field(...) 
    MPa :int = Field(...)
    PSI :int = Field(...)
    KSI : float = Field(...)
    tipoResistencia :str = Field(...,min_length=3,max_length=255)
    clase:Optional[str] = Field(min_length=3, max_length=50)

    class Config:
        anystr_strip_whitespace= True
