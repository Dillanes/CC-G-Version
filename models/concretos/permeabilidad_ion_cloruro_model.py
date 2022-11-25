from pydantic import BaseModel,Field

class permeabilidad_ion_cloruro_model(BaseModel):
    cargaPesada:str = Field(...,min_length=3,max_length=45)
    penetrabilidadIonCloruro:str = Field(...,min_length=3,max_length=45)

    class Config:
        anystr_strip_whitespace = True