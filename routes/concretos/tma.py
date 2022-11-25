from config.messages import Message
from utils.customCrud import CrudFunctions
from utils.customMessages import CustomMessage
from fastapi import APIRouter,Depends
from models.other.default_model import response_petition_model
from models.concretos.tma_model import tma_model
from schemas.other.id_str import all_register,id_str
from auth.jwt_bearer import jwtBearer

msg = Message()

TMA = APIRouter(
    prefix='/api/TMA',
    tags=['TMA'],
    dependencies=[Depends(jwtBearer())]
)


@TMA.get('/',name='TMA',description='get all items',response_model=response_petition_model)
async def get_all_register():
    try:
        data = CrudFunctions.get_all_register('TMA')
        result = all_register(data)
        return CustomMessage(200,msg.msg_get,result) 
    except:
        CustomMessage(400,'ocurrio un error')


@TMA.get('/{id}',name='TMA',description='get single item',response_model=response_petition_model)
def get_one_register(id:str):
    try:
        data = CrudFunctions.get_single_register('TMA',id,where='TMA')
        return CustomMessage(200,msg.msg_get,id_str(data))
    except:
        CustomMessage(400,'id no valido')

        
@TMA.post('/',description='post item', name='post item',response_model=response_petition_model)
def post_regsiter(item:tma_model):
    try:
        id =  CrudFunctions.post_register('TMA',item,True)
        return CustomMessage(201,msg.msg_add,{'_id':str(id)},'TMA')
    except:
        CustomMessage(400,'id no valido')

@TMA.put('/{id}',description='put item', name='put item',response_model=response_petition_model)
def put_register(id:str,body:tma_model):
    try:
        item  = CrudFunctions.put_register('TMA',id,body,'TMA')
        print('*************',item)
        return CustomMessage(200,msg.msg_update)
    except:
        CustomMessage(400,'ocurrio un error')



@TMA.delete('/{id}',name='TMA',description='delete item',response_model=response_petition_model)
def get_one_register(id:str):
    try:
        data = CrudFunctions.delete_register('TMA',id,True,where='TMA')
        if data > 0:
            return CustomMessage(200,msg.msg_delete)
        CustomMessage(400,'No su pudo eliminar')
    except:
        CustomMessage(400,'ocurrio un error')