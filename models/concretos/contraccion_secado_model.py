from pydantic import BaseModel,Field

class contraccion_secado_model(BaseModel):
    contraccionSecado:float = Field(...)
    tipoClase:str = Field(...,min_length=3, max_length=55)

    class Config:
        anystr_strip_whitespace = True



