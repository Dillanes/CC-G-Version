from config.messages import Message
from utils.customCrud import CrudFunctions
from utils.customMessages import CustomMessage
from fastapi import APIRouter,Depends
from fastapi.encoders import jsonable_encoder
from models.other.default_model import response_petition_model
from models.concretos.concretoPremezclado.concreto_premezclado_model import concreto_premezclado_model
from schemas.other.id_str import all_register,id_str
from utils.customValidatorId import verify_register_id_exists
from utils.createStringIds import createStringIds
from config.config_env import Settings
import secrets
from auth.jwt_bearer import jwtBearer

msg = Message()
settings_env = Settings()
concretoPremezclado = APIRouter(
    prefix='/api/concretoPremezclado',
    tags=['concretoPremezclado'],
    dependencies=[Depends(jwtBearer())]
)



@concretoPremezclado.get('/',name='concretoPremezclado',description='get all items',response_model=response_petition_model)
async def get_all_register():
    try:
        data = CrudFunctions.get_all_register('concretoPremezclado')
        result = all_register(data)
        return CustomMessage(200,msg.msg_get,result) 
    except:
        CustomMessage(400,'ocurrio un error')


# @agregado.get('/{id}',name='agregado',description='get single item',response_model=response_petition_model)
# def get_one_register(id:str):
#     try:
#         data = CrudFunctions.get_single_register('agregado',id,where='agregado')
#         return CustomMessage(200,msg.msg_get,id_str(data))
#     except:
#         CustomMessage(400,'id no valido')



    
    # if CrudFunctions.get_single_register('resistenciaConcreto',new_user['id_cp']) is None:
    #     CustomMessage(400,'ID of cp not exists',Where='Register User')
    # if CrudFunctions.get_single_register('departamento',new_user['id_departamento']) is None:
    #     CustomMessage(400,'ID of departament not exists',Where='Register User')
    # return new_user
        
@concretoPremezclado.post('/',description='post item', name='post item')
def post_regsiter(item:concreto_premezclado_model):
    new_cementoP = verify_register_id_exists(item)
    codeStr = createStringIds(new_cementoP)
    new_cementoP['identificador'] = codeStr
    if not CrudFunctions.get_single_register_to_identify('concretoPremezclado',new_cementoP) is None:
        CustomMessage(resiveStatus=400,detailMessagge="Este registro ya existe",method='post',Where="concretoPremezclado")
    try:
        id =  CrudFunctions.post_register('concretoPremezclado',new_cementoP,True)
        return CustomMessage(201,msg.msg_add,{'_id':str(id)},'concretoPremezclado')
    except:
        CustomMessage(400,'id no valido')

# @agregado.put('/{id}',description='put item', name='put item',response_model=response_petition_model)
# def put_register(id:str,body:agregado_model):
#     try:
#         item  = CrudFunctions.put_register('agregado',id,body,'agregado')
#         print('*************',item)
#         return CustomMessage(200,msg.msg_update)
#     except:
#         CustomMessage(400,'ocurrio un error')



@concretoPremezclado.delete('/{id}',name='concretoPremezclado',description='delete item',response_model=response_petition_model)
def get_one_register(id:str):
    try:
        data = CrudFunctions.delete_register('concretoPremezclado',id,True,where='concretoPremezclado')
        if data > 0:
            return CustomMessage(200,msg.msg_delete)
        CustomMessage(400,'No su pudo eliminar')
    except:
        CustomMessage(400,'ocurrio un error')