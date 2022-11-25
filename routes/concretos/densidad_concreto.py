from config.messages import Message
from utils.customCrud import CrudFunctions
from utils.customMessages import CustomMessage
from fastapi import APIRouter,Depends
from models.other.default_model import response_petition_model
from models.concretos.densidad_concreto_model import densidad_concreto_model
from schemas.other.id_str import all_register,id_str
from auth.jwt_bearer import jwtBearer

msg = Message()

densidadConcreto = APIRouter(
    prefix='/api/densidadConcreto',
    tags=['densidadConcreto'],
    dependencies=[Depends(jwtBearer())]
)


@densidadConcreto.get('/',name='densidadConcreto',description='get all items',response_model=response_petition_model)
async def get_all_register():
    try:
        data = CrudFunctions.get_all_register('densidadConcreto')
        result = all_register(data)
        return CustomMessage(200,msg.msg_get,result) 
    except:
        CustomMessage(400,'ocurrio un error')


@densidadConcreto.get('/{id}',name='densidadConcreto',description='get single item',response_model=response_petition_model)
def get_one_register(id:str):
    try:
        data = CrudFunctions.get_single_register('densidadConcreto',id,where='densidadConcreto')
        return CustomMessage(200,msg.msg_get,id_str(data))
    except:
        CustomMessage(400,'id no valido')

        
@densidadConcreto.post('/',description='post item', name='post item',response_model=response_petition_model)
def post_regsiter(item:densidad_concreto_model):
    try:
        id =  CrudFunctions.post_register('densidadConcreto',item,True)
        return CustomMessage(201,msg.msg_add,{'_id':str(id)},'densidadConcreto')
    except:
        CustomMessage(400,'id no valido')

@densidadConcreto.put('/{id}',description='put item', name='put item',response_model=response_petition_model)
def put_register(id:str,body:densidad_concreto_model):
    try:
        item  = CrudFunctions.put_register('densidadConcreto',id,body,'densidadConcreto')
        print('*************',item)
        return CustomMessage(200,msg.msg_update)
    except:
        CustomMessage(400,'ocurrio un error')



@densidadConcreto.delete('/{id}',name='densidadConcreto',description='delete item',response_model=response_petition_model)
def get_one_register(id:str):
    try:
        data = CrudFunctions.delete_register('densidadConcreto',id,True,where='densidadConcreto')
        if data > 0:
            return CustomMessage(200,msg.msg_delete)
        CustomMessage(400,'No su pudo eliminar')
    except:
        CustomMessage(400,'ocurrio un error')