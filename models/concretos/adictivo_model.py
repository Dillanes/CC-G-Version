from pydantic import BaseModel,Field
from typing  import Optional

class adictivo_model(BaseModel):
    adictivo: str = Field(...,min_length=3,max_length=50)
    tipoAdicitivo:str = Field(...,min_length=3,max_length=50)
    aplicaciones :str = Field(...,min_length=3,max_length=255)
    comentario:Optional[str]

    class Config:
        anystr_strip_whitespace = True