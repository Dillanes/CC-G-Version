from pydantic import BaseModel,Field,validator
from typing import Optional
from bson import ObjectId

class concreto_premezclado_modelDef (BaseModel):
    codigoOmniclass:str = Field(...)
    codigoCyC:str = Field(...)
    desCorta:str = Field(...)
    fk_resitenciaCompresion:str = Field(...)
    fk_moduloElasticidad:str = Field(...)
    fk_edadResistencia:str = Field(...)



class concreto_premezclado_model(BaseModel):
    codigoOmniclass:str = Field(...)
    codigoBimsa:str = Field(...)
    codigoCyC:str = Field(...)
    desCorta:str = Field(...,min_length=5,max_length=100)
    desCortaIngles:str = Field(...,min_length=5,max_length=100)
    desLarga:str = Field(...,min_length=5,max_length=255)
    desLargaIngles:str = Field(...,min_length=5,max_length=255)
    uso: Optional[str] = Field(...,min_length=5,max_length=255)
    materialcol:Optional[str] = Field(...,min_length=5,max_length=255)
    fk_resistenciaConcreto:str = Field(...)
    fk_edadResistencia:str = Field(...)
    fk_moduloElasticidad:str= Field(...)
    fk_densidadConcreto:str = Field(...)
    fk_revenimiento :str = Field(...)
    fk_contraccionSecado:str= Field(...)
    fk_agregado:str= Field(...)
    fk_fibra:str= Field(...)
    fk_TMA:str= Field(...)
    fk_adictivo:str= Field(...)
    fk_colocacionConcreto:str= Field(...)
    fk_claseExposicion:str= Field(...)
    fk_permeabilidadIonCloruro:str= Field(...)
    fk_cemento:str= Field(...)

    @validator('fk_resistenciaConcreto',
                'fk_edadResistencia',
                'fk_moduloElasticidad',
                'fk_densidadConcreto',
                'fk_revenimiento',
                'fk_contraccionSecado',
                'fk_agregado',
                'fk_fibra',
                'fk_TMA',
                'fk_adictivo',
                'fk_colocacionConcreto',
                'fk_claseExposicion',
                'fk_permeabilidadIonCloruro',
                'fk_cemento'
                )
                
    def validator_id(cls, v,):
        if ObjectId.is_valid(v):
            return v
        raise ValueError('Id no valido')

    





