from config.messages import Message
from utils.customCrud import CrudFunctions
from utils.customMessages import CustomMessage
from fastapi import APIRouter,Depends
from models.other.default_model import response_petition_model
from models.concretos.cemento_model import cemento_model
from schemas.other.id_str import all_register,id_str
from auth.jwt_bearer import jwtBearer

msg = Message()

cemento = APIRouter(
    prefix='/api/cemento',
    tags=['cemento'],
    dependencies=[Depends(jwtBearer())]
)


@cemento.get('/',name='cemento',description='get all items',response_model=response_petition_model)
async def get_all_register():
    try:
        data = CrudFunctions.get_all_register('cemento')
        result = all_register(data)
        return CustomMessage(200,msg.msg_get,result) 
    except:
        CustomMessage(400,'ocurrio un error')


@cemento.get('/{id}',name='cemento',description='get single item',response_model=response_petition_model)
def get_one_register(id:str):
    try:
        data = CrudFunctions.get_single_register('cemento',id,where='cemento')
        return CustomMessage(200,msg.msg_get,id_str(data))
    except:
        CustomMessage(400,'id no valido')

        
@cemento.post('/',description='post item', name='post item',response_model=response_petition_model)
def post_regsiter(item:cemento_model):
    try:
        id =  CrudFunctions.post_register('cemento',item,True)
        return CustomMessage(201,msg.msg_add,{'_id':str(id)},'cemento')
    except:
        CustomMessage(400,'id no valido')

@cemento.put('/{id}',description='put item', name='put item',response_model=response_petition_model)
def put_register(id:str,body:cemento_model):
    try:
        item  = CrudFunctions.put_register('cemento',id,body,'cemento')
        print('*************',item)
        return CustomMessage(200,msg.msg_update)
    except:
        CustomMessage(400,'ocurrio un error')



@cemento.delete('/{id}',name='cemento',description='delete item',response_model=response_petition_model)
def get_one_register(id:str):
    try:
        data = CrudFunctions.delete_register('cemento',id,True,where='cemento')
        if data > 0:
            return CustomMessage(200,msg.msg_delete)
        CustomMessage(400,'No su pudo eliminar')
    except:
        CustomMessage(400,'ocurrio un error')