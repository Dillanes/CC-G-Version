from pydantic import BaseModel,Field

class tma_model(BaseModel):
    tmaMM:float = Field(...)
    tipoTMA:str = Field(...,max_length=55,min_length=3)
    tmaIN:str = Field(...,max_length=55,min_length=3)

    class Config:
        anystr_strip_whitespace = True
        
         