from config.messages import Message
from utils.customCrud import CrudFunctions
from utils.customMessages import CustomMessage
from fastapi import APIRouter,Depends
from models.other.default_model import response_petition_model
from models.concretos.color_concreto_model import color_concreto_schema
from schemas.other.id_str import all_register,id_str
from auth.jwt_bearer import jwtBearer

msg = Message()

colorConcreto = APIRouter(
    prefix='/api/colorConcreto',
    tags=['colorConcreto'],
    dependencies=[Depends(jwtBearer())]
)


@colorConcreto.get('/',name='colorConcreto',description='get all items',response_model=response_petition_model)
async def get_all_register():
    try:
        data = CrudFunctions.get_all_register('colorConcreto')
        result = all_register(data)
        return CustomMessage(200,msg.msg_get,result) 
    except:
        CustomMessage(400,'ocurrio un error')


@colorConcreto.get('/{id}',name='colorConcreto',description='get single item',response_model=response_petition_model)
def get_one_register(id:str):
    try:
        data = CrudFunctions.get_single_register('colorConcreto',id,where='colorConcreto')
        return CustomMessage(200,msg.msg_get,id_str(data))
    except:
        CustomMessage(400,'id no valido')

        
@colorConcreto.post('/',description='post item', name='post item',response_model=response_petition_model)
def post_regsiter(item:color_concreto_schema):
    try:
        id =  CrudFunctions.post_register('colorConcreto',item,True)
        return CustomMessage(201,msg.msg_add,{'_id':str(id)},'colorConcreto')
    except:
        CustomMessage(400,'id no valido')

@colorConcreto.put('/{id}',description='put item', name='put item',response_model=response_petition_model)
def put_register(id:str,body:color_concreto_schema):
    try:
        item  = CrudFunctions.put_register('colorConcreto',id,body,'colorConcreto')
        print('*************',item)
        return CustomMessage(200,msg.msg_update)
    except:
        CustomMessage(400,'ocurrio un error')



@colorConcreto.delete('/{id}',name='colorConcreto',description='delete item',response_model=response_petition_model)
def get_one_register(id:str):
    try:
        data = CrudFunctions.delete_register('colorConcreto',id,True,where='colorConcreto')
        if data > 0:
            return CustomMessage(200,msg.msg_delete)
        CustomMessage(400,'No su pudo eliminar')
    except:
        CustomMessage(400,'ocurrio un error')