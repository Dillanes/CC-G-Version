from config.messages import Message
from utils.customCrud import CrudFunctions
from utils.customMessages import CustomMessage
from fastapi import APIRouter,Depends
from models.other.default_model import response_petition_model
from models.concretos.clase_exposicion import clase_exposicion_model
from schemas.other.id_str import all_register,id_str
from auth.jwt_bearer import jwtBearer

msg = Message()

claseExposicion = APIRouter(
    prefix='/api/claseExposicion',
    tags=['claseExposicion'],
    dependencies=[Depends(jwtBearer())]
)


@claseExposicion.get('/',name='claseExposicion',description='get all items',response_model=response_petition_model)
async def get_all_register():
    try:
        data = CrudFunctions.get_all_register('claseExposicion')
        result = all_register(data)
        return CustomMessage(200,msg.msg_get,result) 
    except:
        CustomMessage(400,'ocurrio un error')


@claseExposicion.get('/{id}',name='claseExposicion',description='get single item',response_model=response_petition_model)
def get_one_register(id:str):
    try:
        data = CrudFunctions.get_single_register('claseExposicion',id,where='claseExposicion')
        return CustomMessage(200,msg.msg_get,id_str(data))
    except:
        CustomMessage(400,'id no valido')

        
@claseExposicion.post('/',description='post item', name='post item',response_model=response_petition_model)
def post_regsiter(item:clase_exposicion_model):
    try:
        id =  CrudFunctions.post_register('claseExposicion',item,True)
        return CustomMessage(201,msg.msg_add,{'_id':str(id)},'claseExposicion')
    except:
        CustomMessage(400,'id no valido')

@claseExposicion.put('/{id}',description='put item', name='put item',response_model=response_petition_model)
def put_register(id:str,body:clase_exposicion_model):
    try:
        item  = CrudFunctions.put_register('claseExposicion',id,body,'claseExposicion')
        print('*************',item)
        return CustomMessage(200,msg.msg_update)
    except:
        CustomMessage(400,'ocurrio un error')



@claseExposicion.delete('/{id}',name='claseExposicion',description='delete item',response_model=response_petition_model)
def get_one_register(id:str):
    try:
        data = CrudFunctions.delete_register('claseExposicion',id,True,where='claseExposicion')
        if data > 0:
            return CustomMessage(200,msg.msg_delete)
        CustomMessage(400,'No su pudo eliminar')
    except:
        CustomMessage(400,'ocurrio un error')