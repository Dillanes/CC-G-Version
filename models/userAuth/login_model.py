from pydantic import BaseModel,EmailStr,Field

class login_user(BaseModel):
    email:EmailStr = Field(...)
    password:str= Field(...,min_length=3,max_length=50)