from config.messages import Message
from utils.customCrud import CrudFunctions
from utils.customMessages import CustomMessage
from fastapi import APIRouter,Depends
from schemas.concretos.edad_resistencia_schema import all_edad_resistencia_schema,edad_resistencia_schema
from models.other.default_model import response_petition_model
from models.concretos.edad_resistencia_model import edad_resistencia_model
from auth.jwt_bearer import jwtBearer

msg = Message()

edadResistencia = APIRouter(
    prefix='/api/edadResistencia',
    tags=['edadResistencia'],
    dependencies=[Depends(jwtBearer())]
)



@edadResistencia.get('/',name='edadResistencia',description='get all adictivos',response_model=response_petition_model)
def get_all_register():
    try:
        data = CrudFunctions.get_all_register('edadResistencia')
        return CustomMessage(200,msg.msg_get,all_edad_resistencia_schema(data)) 
    except:
        CustomMessage(400,'ocurrio un error')

@edadResistencia.get('/{id}',name='edadResistencia',description='get all adictivos',response_model=response_petition_model)
def get_one_register(id:str):
    try:
        data = CrudFunctions.get_single_register('edadResistencia',id,where='edadResistencia')
        return CustomMessage(200,msg.msg_get,edad_resistencia_schema(data)) 
    except:
        CustomMessage(400,'ocurrio un error')
        
@edadResistencia.post('/',description='post item', name='post item',response_model=response_petition_model)
def post_regsiter(item:edad_resistencia_model):
    try:
        id =  CrudFunctions.post_register('edadResistencia',item,True)
        return CustomMessage(201,msg.msg_add,{'_id':str(id)},'edadResistencia')
    except:
        CustomMessage(400,'ocurrio un error')

@edadResistencia.put('/{id}',description='put item', name='put item',response_model=response_petition_model)
def put_register(id:str,body:edad_resistencia_model):
    try:
        item  = CrudFunctions.put_register('edadResistencia',id,body,'edadResistencia')
        print('*************',item)
        return CustomMessage(200,msg.msg_update)
    except:
        CustomMessage(400,'ocurrio un error')



@edadResistencia.delete('/{id}',name='edadResistencia',description='get all adictivos',response_model=response_petition_model)
def get_one_register(id:str):
    try:
        data = CrudFunctions.delete_register('edadResistencia',id,True,where='edadResistencia')
        if data > 0:
            return CustomMessage(200,msg.msg_delete)
        CustomMessage(400,'No su pudo eliminar')
    except:
        CustomMessage(400,'ocurrio un error')
