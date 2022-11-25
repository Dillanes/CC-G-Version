from pydantic import BaseModel,Field

class agregado_model(BaseModel):
    agregado :str = Field(...,min_length=3,max_length=55)
    tipoAgregado:str = Field(...,min_length=3,max_length=55)
    origen:str = Field(...,min_length=3,max_length=55)


    class Config:
        anystr_strip_whitespace = True

