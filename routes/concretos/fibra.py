from config.messages import Message
from utils.customCrud import CrudFunctions
from utils.customMessages import CustomMessage
from fastapi import APIRouter,Depends
from models.other.default_model import response_petition_model
from models.concretos.fibra_model import fibra_model
from schemas.other.id_str import all_register,id_str
from auth.jwt_bearer import jwtBearer

msg = Message()

fibra = APIRouter(
    prefix='/api/fibra',
    tags=['fibra'],
    dependencies=[Depends(jwtBearer())]
)


@fibra.get('/',name='fibra',description='get all items',response_model=response_petition_model)
async def get_all_register():
    try:
        data = CrudFunctions.get_all_register('fibra')
        result = all_register(data)
        return CustomMessage(200,msg.msg_get,result) 
    except:
        CustomMessage(400,'ocurrio un error')


@fibra.get('/{id}',name='fibra',description='get single item',response_model=response_petition_model)
def get_one_register(id:str):
    try:
        data = CrudFunctions.get_single_register('fibra',id,where='fibra')
        return CustomMessage(200,msg.msg_get,id_str(data))
    except:
        CustomMessage(400,'id no valido')

        
@fibra.post('/',description='post item', name='post item',response_model=response_petition_model)
def post_regsiter(item:fibra_model):
    try:
        id =  CrudFunctions.post_register('fibra',item,True)
        return CustomMessage(201,msg.msg_add,{'_id':str(id)},'fibra')
    except:
        CustomMessage(400,'id no valido')

@fibra.put('/{id}',description='put item', name='put item',response_model=response_petition_model)
def put_register(id:str,body:fibra_model):
    try:
        item  = CrudFunctions.put_register('fibra',id,body,'fibra')

        return CustomMessage(200,msg.msg_update)
    except:
        CustomMessage(400,'ocurrio un error')



@fibra.delete('/{id}',name='fibra',description='delete item',response_model=response_petition_model)
def get_one_register(id:str):
    try:
        data = CrudFunctions.delete_register('fibra',id,True,where='fibra')
        if data > 0:
            return CustomMessage(200,msg.msg_delete)
        CustomMessage(400,'No su pudo eliminar')
    except:
        CustomMessage(400,'ocurrio un error')