from config.messages import Message
from utils.customCrud import CrudFunctions
from utils.customMessages import CustomMessage
from fastapi import APIRouter,Depends
from schemas.concretos.adictivo import all_adictivo_schema,adictivo_schema
from models.other.default_model import response_petition_model
from models.concretos.adictivo_model import adictivo_model
from auth.jwt_bearer import jwtBearer
from schemas.other.id_str import all_register,id_str


msg = Message()
adictivo = APIRouter(
    prefix='/api/adictivo',
    tags=['adictivo'],
    dependencies=[Depends(jwtBearer())]
    
)

@adictivo.get('/',name='adictivo',description='get all items',response_model=response_petition_model)
async def get_all_register():
    try:
        data = CrudFunctions.get_all_register('adictivo')
        result = all_register(data)
        return CustomMessage(200,msg.msg_get,result) 
    except:
        CustomMessage(400,'ocurrio un error')

@adictivo.get('/{id}',name='adictivo',description='get single item',response_model=response_petition_model)
def get_one_register(id:str):
    try:
        data = CrudFunctions.get_single_register('adictivo',id,where='adictivo')
        return CustomMessage(200,msg.msg_get,id_str(data))
    except:
        CustomMessage(400,'id no valido')
        
        
@adictivo.post('/',description='post item', name='post item',response_model=response_petition_model)
def post_regsiter(item:adictivo_model):
    try:
        id =  CrudFunctions.post_register('adictivo',item,True)
        return CustomMessage(201,msg.msg_add,{'_id':str(id)},'adictivo')
    except:
        CustomMessage(400,'ocurrio un error')

@adictivo.put('/{id}',description='put item', name='put item',response_model=response_petition_model)
def put_register(id:str,body:adictivo_model):
    try:
        item  = CrudFunctions.put_register('adictivo',id,body,'adictivo')
        print('*************',item)
        return CustomMessage(200,msg.msg_update)
    except:
        CustomMessage(400,'ocurrio un error')







@adictivo.delete('/{id}',name='adictivo',description='get all adictivos',response_model=response_petition_model)
def get_one_register(id:str):
    try:
        data = CrudFunctions.delete_register('adictivo',id,True,where='adictivo')
        if data > 0:
            return CustomMessage(200,msg.msg_delete)
        CustomMessage(400,'No su pudo eliminar')
    except:
        CustomMessage(400,'ocurrio un error')



