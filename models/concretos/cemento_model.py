from pydantic import BaseModel,Field

class cemento_model(BaseModel):
    tipoCemento:str = Field(...,min_length=3,max_length=55)

    class Config:
        anystr_strip_whitespace = True