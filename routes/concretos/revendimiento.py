from config.messages import Message
from utils.customCrud import CrudFunctions
from utils.customMessages import CustomMessage
from fastapi import APIRouter,Depends
from models.other.default_model import response_petition_model
from models.concretos.revenimiento_model import revendimiento_model
from schemas.other.id_str import all_register,id_str
from auth.jwt_bearer import jwtBearer

msg = Message()

revenimiento = APIRouter(
    prefix='/api/revenimiento',
    tags=['revenimiento'],
    dependencies=[Depends(jwtBearer())]
)


@revenimiento.get('/',name='revenimiento',description='get all items',response_model=response_petition_model)
async def get_all_register():
    try:
        data = CrudFunctions.get_all_register('revenimiento')
        result = all_register(data)
        return CustomMessage(200,msg.msg_get,result) 
    except:
        CustomMessage(400,'ocurrio un error')


@revenimiento.get('/{id}',name='revenimiento',description='get single item',response_model=response_petition_model)
def get_one_register(id:str):
    try:
        data = CrudFunctions.get_single_register('revenimiento',id,where='revenimiento')
        return CustomMessage(200,msg.msg_get,id_str(data))
    except:
        CustomMessage(400,'id no valido')

        
@revenimiento.post('/',description='post item', name='post item',response_model=response_petition_model)
def post_regsiter(item:revendimiento_model):
    try:
        id =  CrudFunctions.post_register('revenimiento',item,True)
        return CustomMessage(201,msg.msg_add,{'_id':str(id)},'revenimiento')
    except:
        CustomMessage(400,'id no valido')

@revenimiento.put('/{id}',description='put item', name='put item',response_model=response_petition_model)
def put_register(id:str,body:revendimiento_model):
    try:
        item  = CrudFunctions.put_register('revenimiento',id,body,'revenimiento')
        print('*************',item)
        return CustomMessage(200,msg.msg_update)
    except:
        CustomMessage(400,'ocurrio un error')



@revenimiento.delete('/{id}',name='revenimiento',description='delete item',response_model=response_petition_model)
def get_one_register(id:str):
    try:
        data = CrudFunctions.delete_register('revenimiento',id,True,where='revenimiento')
        if data > 0:
            return CustomMessage(200,msg.msg_delete)
        CustomMessage(400,'No su pudo eliminar')
    except:
        CustomMessage(400,'ocurrio un error')