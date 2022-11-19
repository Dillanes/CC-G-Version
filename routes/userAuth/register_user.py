from fastapi import APIRouter,status
from config.messages import Message
from utils.customMessages import CustomMessage
from utils.customCrud import CrudFunctions
from fastapi.encoders import jsonable_encoder
from bson import ObjectId
from models.userAuth.user_register_model import register_user_model
from passlib.hash import pbkdf2_sha256
from schemas.userAuth.colonia_schema import insert_colonia_schema
from schemas.userAuth.empleado_schema import insert_empleado_schema
from schemas.userAuth.persona_schema import insert_persona_schema
from models.other.default_model import response_petition_model


msg = Message()

#create rute to register user
userRegiter = APIRouter(
    tags=['Registro de usuario'],
    prefix='/api/sing'
)


#VERIFY THAT THE DNI IS VALID
def verify_user_ids(body:register_user_model):
    new_user = jsonable_encoder(body)
    if not ObjectId.is_valid(new_user['id_cp']):
        CustomMessage(400,'Id Cp no valido',Where='Register User')
    if not ObjectId.is_valid(new_user['id_departamento']):
        CustomMessage(400,'Id Departamento no valido',Where='Register User')
    if CrudFunctions.get_single_register('codigoPostal',new_user['id_cp']) is None:
        CustomMessage(400,'ID of cp not exists',Where='Register User')
    if CrudFunctions.get_single_register('departamento',new_user['id_departamento']) is None:
        CustomMessage(400,'ID of departament not exists',Where='Register User')
    return new_user



#FUNCION ADD USER
#USE DOCUMENTS: COLONIA,PERSONA,EMPLEADO
@userRegiter.post('/',name='Insert data user',status_code=status.HTTP_201_CREATED,response_model=response_petition_model)
def register_user(body:register_user_model):
    user_exists = CrudFunctions.get_single_register(nameDocument='empleado',register=body,where='Register User Email')
    if  user_exists:
        CustomMessage(400,'The email address alrady exist',Where='empleado',method='post')
    
    #use function verify_user_ids
    new_user = verify_user_ids(body)
    
    

    persona = insert_persona_schema(new_user)
    empleado = insert_empleado_schema(new_user)
    colonia = insert_colonia_schema(new_user)

    print('**********',persona)
    print('**********',empleado)
    print('**********',colonia)

    return CustomMessage(resiveStatus=201, detailMessagge='Correct')


    # id_colonia = CrudFunctions.post_register('colonia',colonia,True)
    # if id_colonia is None:
    #     CustomMessage(400,msg.msg_error_add,Where='Register user',method='post')
    # persona['id_colonia'] = str(id_colonia) 
    # id_person = CrudFunctions.post_register('persona',persona,True)
    # if id_person is None:
    #     CustomMessage(400,msg.msg_error_add,Where='Register user',method='post')
    # empleado['id_per'] = str(id_person)
    # empleado['password'] = pbkdf2_sha256.hash(empleado['password'])
    # id_empleado = CrudFunctions.post_register('empleado',empleado,True)
    # if id_empleado is None:
    #     CustomMessage(400,msg.msg_error_add,Where='empleado',method='post')
    # return CustomMessage(201,detailMessagge=msg.msg_add,data={'_id':str(id_empleado)},Where='registerUser',method='post')

