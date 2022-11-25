from pydantic import BaseModel,Field


class color_concreto_schema(BaseModel):
    color:str = Field(...)
    absorcionCapilar:int = Field(...)
    tiempoTrabajabilidadExtendida: float = Field(...)
    tansmiteLuz:bool = Field(default=False)
    coeficienteDilatacionTermica:str = Field(...,min_length=5, max_length=45)
    emisivilidad:float = Field(...)
    permeabilidadAgua:float = Field(...)
    flexivilidad:float = Field(...)
    resistivilidadElectricaOhmios:str = Field(...,min_length=5, max_length=45)
    resistivilidadElectricaDias:int = Field(...)
    contenidoCloruro:float = Field(...)
    comportamiento:str = Field(...,min_length=5, max_length=45)
    contenidoAire:float = Field(...)
    conductividadTermicaKcalm2hc:str = Field(...,min_length=5, max_length=45)
    conductividadTermica_wm2k:str= Field(...,min_length=5, max_length=45)
    calorEspecifico_JKGc:float = Field(...)

    class Config:
        anystr_strip_whitespace = True

        