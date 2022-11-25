from config.messages import Message
from utils.customCrud import CrudFunctions
from utils.customMessages import CustomMessage
from fastapi import APIRouter,Depends
from models.other.default_model import response_petition_model
from models.concretos.agregado_model import agregado_model
from schemas.other.id_str import all_register,id_str
from auth.jwt_bearer import jwtBearer

msg = Message()

agregado = APIRouter(
    prefix='/api/agregado',
    tags=['agregado'],
    dependencies=[Depends(jwtBearer())]
)


@agregado.get('/',name='agregado',description='get all items',response_model=response_petition_model)
async def get_all_register():
    try:
        data = CrudFunctions.get_all_register('agregado')
        result = all_register(data)
        return CustomMessage(200,msg.msg_get,result) 
    except:
        CustomMessage(400,'ocurrio un error')


@agregado.get('/{id}',name='agregado',description='get single item',response_model=response_petition_model)
def get_one_register(id:str):
    try:
        data = CrudFunctions.get_single_register('agregado',id,where='agregado')
        return CustomMessage(200,msg.msg_get,id_str(data))
    except:
        CustomMessage(400,'id no valido')

        
@agregado.post('/',description='post item', name='post item',response_model=response_petition_model)
def post_regsiter(item:agregado_model):
    try:
        id =  CrudFunctions.post_register('agregado',item,True)
        return CustomMessage(201,msg.msg_add,{'_id':str(id)},'agregado')
    except:
        CustomMessage(400,'id no valido')

@agregado.put('/{id}',description='put item', name='put item',response_model=response_petition_model)
def put_register(id:str,body:agregado_model):
    try:
        item  = CrudFunctions.put_register('agregado',id,body,'agregado')
        print('*************',item)
        return CustomMessage(200,msg.msg_update)
    except:
        CustomMessage(400,'ocurrio un error')



@agregado.delete('/{id}',name='agregado',description='delete item',response_model=response_petition_model)
def get_one_register(id:str):
    try:
        data = CrudFunctions.delete_register('agregado',id,True,where='agregado')
        if data > 0:
            return CustomMessage(200,msg.msg_delete)
        CustomMessage(400,'No su pudo eliminar')
    except:
        CustomMessage(400,'ocurrio un error')