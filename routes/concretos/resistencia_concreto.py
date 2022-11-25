from config.messages import Message
from utils.customCrud import CrudFunctions
from utils.customMessages import CustomMessage
from fastapi import APIRouter,Depends
# from schemas.concretos.resistencia_concreto_schema import all_resistencia_concreto_schema,resistencia_concreto_schema
from models.other.default_model import response_petition_model
from models.concretos.resistencia_concreto_model import resistencia_concreto_model
from schemas.other.id_str import all_register,id_str
from auth.jwt_bearer import jwtBearer

msg = Message()

resistenciaConcreto = APIRouter(
    prefix='/api/resistenciaConcreto',
    tags=['resistenciaConcreto'],
    dependencies=[Depends(jwtBearer())]
)


@resistenciaConcreto.get('/',name='resistenciaConcreto',description='get all adictivos',response_model=response_petition_model)
async def get_all_register():
    try:
        data = CrudFunctions.get_all_register('resistenciaConcreto')
        result = all_register(data)
        return CustomMessage(200,msg.msg_get,result) 
    except:
        CustomMessage(400,'ocurrio un error')


@resistenciaConcreto.get('/{id}',name='resistenciaConcreto',description='get all adictivos',response_model=response_petition_model)
def get_one_register(id:str):
    try:
        data = CrudFunctions.get_single_register('resistenciaConcreto',id,where='resistenciaConcreto')
        return CustomMessage(200,msg.msg_get,id_str(data))
    except:
        CustomMessage(400,'id no valido')

        
@resistenciaConcreto.post('/',description='post item', name='post item',response_model=response_petition_model)
def post_regsiter(item:resistencia_concreto_model):
    try:
        id =  CrudFunctions.post_register('resistenciaConcreto',item,True)
        return CustomMessage(201,msg.msg_add,{'_id':str(id)},'resistenciaConcreto')
    except:
        CustomMessage(400,'id no valido')

@resistenciaConcreto.put('/{id}',description='put item', name='put item',response_model=response_petition_model)
def put_register(id:str,body:resistencia_concreto_model):
    try:
        item  = CrudFunctions.put_register('resistenciaConcreto',id,body,'resistenciaConcreto')
        print('*************',item)
        return CustomMessage(200,msg.msg_update)
    except:
        CustomMessage(400,'ocurrio un error')



@resistenciaConcreto.delete('/{id}',name='resistenciaConcreto',description='get all adictivos',response_model=response_petition_model)
def get_one_register(id:str):
    try:
        data = CrudFunctions.delete_register('resistenciaConcreto',id,True,where='resistenciaConcreto')
        if data > 0:
            return CustomMessage(200,msg.msg_delete)
        CustomMessage(400,'No su pudo eliminar')
    except:
        CustomMessage(400,'ocurrio un error')
