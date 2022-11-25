from pydantic import BaseModel,Field
from typing import Optional


class modulo_elasticidad_model(BaseModel):
    MPa:float = Field(...)
    PSI:float = Field(...)
    kgcm2 :float = Field(...)
    comentario:Optional[str] = Field(min_length=3,max_length=255)

    class Config:
        anystr_strip_whitespace = True


