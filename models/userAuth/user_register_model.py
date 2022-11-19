from pydantic import BaseModel,Field,EmailStr,validator
from typing import Optional
from datetime import date,datetime
from bson import ObjectId


class register_user_model(BaseModel):
    nombre:str = Field(...,min_length=3,max_length=50)
    apellido_p:str =  Field(...,min_length=3,max_length=50)
    apellido_m:str =  Field(...,min_length=3,max_length=50)
    genero:str =   Field(...,min_length=1,max_length=1)
    fecha_nacimiento:date = Field(...)
    tel:str =  Field(...,min_length=8,max_length=16)
    curp:str =  Field(...,min_length=18,max_length=18)
    rfc:str =  Field(...,min_length=12,max_length=13)
    cargo:str = Field(...)
    email:EmailStr = Field(...)
    password:str = Field(...,min_length=3,max_length=50)
    date_register:Optional[date] = datetime.today()
    last_login:Optional[datetime] = None
    is_active:Optional[bool] = Field(default=False)
    colonia:str = Field(...,min_length=3,max_length=50)
    calle:str = Field(...,min_length=3,max_length=50)
    no_int:int = Field(...)
    no_ext:int = Field(...)
    id_cp:str = Field(...)
    id_departamento:str = Field(...)

    class Cofig:
        anystr_strip_whitespace = True

    @validator('genero')
    def validate_genero(cls,genero):
        new_genero = genero.upper()
        if new_genero == 'M' or new_genero == 'H':
            return new_genero
        raise ValueError('Tipo de dato no valido, asegurate de enviar M(Mujer) o H(Hombre)')
    
    @validator('cargo')
    def validate_cargo(cls,cargo):
        new_cargo = cargo.lower()
        if new_cargo == 'admin' or new_cargo == 'empleado':
            return cargo
        raise ValueError('Tipo de cargo no valido intenta enviando, admin o empleado')
    
    @validator('no_int')
    def validate_no_int(cls,no_int):
        if no_int < 1:
            raise ValueError('not_int no valido: asegurate de enviar un valor mayor a 0')
        no_int_text = str(no_int)
        if len(no_int_text) < 5 and len(no_int_text)>1:
            return no_int
        raise ValueError('not_int invalid: make sure its length is greater than one and less than 5')

    @validator('no_ext')
    def validate_no_ext(cls,no_ext):
        if no_ext <1:
            raise ValueError('not_ext no valido: asegurate de enviar un valor mayor a 0')
        no_ext_text = str(no_ext)
        if len(no_ext_text) < 5 and len(no_ext_text)>1:
            return no_ext
        raise ValueError('not_iext invalid: make sure its length is greater than one and less than 5 ')



