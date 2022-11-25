from config.messages import Message
from utils.customCrud import CrudFunctions
from utils.customMessages import CustomMessage
from fastapi import APIRouter,Depends
# from schemas.concretos.resistencia_concreto_schema import all_resistencia_concreto_schema,resistencia_concreto_schema
from models.other.default_model import response_petition_model
from models.concretos.modulo_elasticidad_model import modulo_elasticidad_model
from schemas.other.id_str import all_register,id_str
from auth.jwt_bearer import jwtBearer

msg = Message()

moduloElasticidad = APIRouter(
    prefix='/api/moduloElasticidad',
    tags=['moduloElasticidad'],
    dependencies=[Depends(jwtBearer())]
)


@moduloElasticidad.get('/',name='moduloElasticidad',description='get all adictivos',response_model=response_petition_model)
async def get_all_register():
    try:
        data = CrudFunctions.get_all_register('moduloElasticidad')
        result = all_register(data)
        return CustomMessage(200,msg.msg_get,result) 
    except:
        CustomMessage(400,'ocurrio un error')


@moduloElasticidad.get('/{id}',name='moduloElasticidad',description='get all adictivos',response_model=response_petition_model)
def get_one_register(id:str):
    try:
        data = CrudFunctions.get_single_register('moduloElasticidad',id,where='moduloElasticidad')
        return CustomMessage(200,msg.msg_get,id_str(data))
    except:
        CustomMessage(400,'id no valido')

        
@moduloElasticidad.post('/',description='post item', name='post item',response_model=response_petition_model)
def post_regsiter(item:modulo_elasticidad_model):
    try:
        id =  CrudFunctions.post_register('moduloElasticidad',item,True)
        return CustomMessage(201,msg.msg_add,{'_id':str(id)},'moduloElasticidad')
    except:
        CustomMessage(400,'id no valido')

@moduloElasticidad.put('/{id}',description='put item', name='put item',response_model=response_petition_model)
def put_register(id:str,body:modulo_elasticidad_model):
    try:
        item  = CrudFunctions.put_register('moduloElasticidad',id,body,'moduloElasticidad')
        print('*************',item)
        return CustomMessage(200,msg.msg_update)
    except:
        CustomMessage(400,'ocurrio un error')



@moduloElasticidad.delete('/{id}',name='moduloElasticidad',description='get all adictivos',response_model=response_petition_model)
def get_one_register(id:str):
    try:
        data = CrudFunctions.delete_register('moduloElasticidad',id,True,where='moduloElasticidad')
        if data > 0:
            return CustomMessage(200,msg.msg_delete)
        CustomMessage(400,'No su pudo eliminar')
    except:
        CustomMessage(400,'ocurrio un error')