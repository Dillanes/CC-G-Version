from pydantic import BaseModel,Field

class colocacion_model(BaseModel):
    sistemaColocacion:str = Field(...,min_length=3, max_length=55)
    equipos:str = Field(...,min_length=3, max_length=55)

    class Config:
        anystr_strip_whitespace = True

        