from config.messages import Message
from utils.customCrud import CrudFunctions
from utils.customMessages import CustomMessage
from fastapi import APIRouter,Depends
from models.other.default_model import response_petition_model
from models.concretos.contraccion_secado_model import contraccion_secado_model
from schemas.other.id_str import all_register,id_str
from auth.jwt_bearer import jwtBearer

msg = Message()

contraccionSecado = APIRouter(
    prefix='/api/contraccionSecado',
    tags=['contraccionSecado'],
    dependencies=[Depends(jwtBearer())]
)


@contraccionSecado.get('/',name='contraccionSecado',description='get all items',response_model=response_petition_model)
async def get_all_register():
    try:
        data = CrudFunctions.get_all_register('contraccionSecado')
        result = all_register(data)
        return CustomMessage(200,msg.msg_get,result) 
    except:
        CustomMessage(400,'ocurrio un error')


@contraccionSecado.get('/{id}',name='contraccionSecado',description='get single item',response_model=response_petition_model)
def get_one_register(id:str):
    try:
        data = CrudFunctions.get_single_register('contraccionSecado',id,where='contraccionSecado')
        return CustomMessage(200,msg.msg_get,id_str(data))
    except:
        CustomMessage(400,'id no valido')

        
@contraccionSecado.post('/',description='post item', name='post item',response_model=response_petition_model)
def post_regsiter(item:contraccion_secado_model):
    try:
        id =  CrudFunctions.post_register('contraccionSecado',item,True)
        return CustomMessage(201,msg.msg_add,{'_id':str(id)},'contraccionSecado')
    except:
        CustomMessage(400,'id no valido')

@contraccionSecado.put('/{id}',description='put item', name='put item',response_model=response_petition_model)
def put_register(id:str,body:contraccion_secado_model):
    try:
        item  = CrudFunctions.put_register('contraccionSecado',id,body,'contraccionSecado')
        print('*************',item)
        return CustomMessage(200,msg.msg_update)
    except:
        CustomMessage(400,'ocurrio un error')



@contraccionSecado.delete('/{id}',name='contraccionSecado',description='delete item',response_model=response_petition_model)
def get_one_register(id:str):
    try:
        data = CrudFunctions.delete_register('contraccionSecado',id,True,where='contraccionSecado')
        if data > 0:
            return CustomMessage(200,msg.msg_delete)
        CustomMessage(400,'No su pudo eliminar')
    except:
        CustomMessage(400,'ocurrio un error')