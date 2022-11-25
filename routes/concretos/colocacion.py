from config.messages import Message
from utils.customCrud import CrudFunctions
from utils.customMessages import CustomMessage
from fastapi import APIRouter,Depends
from models.other.default_model import response_petition_model
from models.concretos.colocacion_model import colocacion_model
from schemas.other.id_str import all_register,id_str
from auth.jwt_bearer import jwtBearer

msg = Message()

colocacionConcreto = APIRouter(
    prefix='/api/colocacionConcreto',
    tags=['colocacionConcreto'],
    dependencies=[Depends(jwtBearer())]
)


@colocacionConcreto.get('/',name='colocacionConcreto',description='get all items',response_model=response_petition_model)
async def get_all_register():
    try:
        data = CrudFunctions.get_all_register('colocacionConcreto')
        result = all_register(data)
        return CustomMessage(200,msg.msg_get,result) 
    except:
        CustomMessage(400,'ocurrio un error')


@colocacionConcreto.get('/{id}',name='colocacionConcreto',description='get single item',response_model=response_petition_model)
def get_one_register(id:str):
    try:
        data = CrudFunctions.get_single_register('colocacionConcreto',id,where='colocacionConcreto')
        return CustomMessage(200,msg.msg_get,id_str(data))
    except:
        CustomMessage(400,'id no valido')

        
@colocacionConcreto.post('/',description='post item', name='post item',response_model=response_petition_model)
def post_regsiter(item:colocacion_model):
    try:
        id =  CrudFunctions.post_register('colocacionConcreto',item,True)
        return CustomMessage(201,msg.msg_add,{'_id':str(id)},'colocacionConcreto')
    except:
        CustomMessage(400,'id no valido')

@colocacionConcreto.put('/{id}',description='put item', name='put item',response_model=response_petition_model)
def put_register(id:str,body:colocacion_model):
    try:
        item  = CrudFunctions.put_register('colocacionConcreto',id,body,'colocacionConcreto')
        print('*************',item)
        return CustomMessage(200,msg.msg_update)
    except:
        CustomMessage(400,'ocurrio un error')



@colocacionConcreto.delete('/{id}',name='colocacionConcreto',description='delete item',response_model=response_petition_model)
def get_one_register(id:str):
    try:
        data = CrudFunctions.delete_register('colocacionConcreto',id,True,where='colocacionConcreto')
        if data > 0:
            return CustomMessage(200,msg.msg_delete)
        CustomMessage(400,'No su pudo eliminar')
    except:
        CustomMessage(400,'ocurrio un error')