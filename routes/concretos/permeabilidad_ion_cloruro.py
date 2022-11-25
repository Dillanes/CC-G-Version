from config.messages import Message
from utils.customCrud import CrudFunctions
from utils.customMessages import CustomMessage
from fastapi import APIRouter,Depends
from models.other.default_model import response_petition_model
from models.concretos.permeabilidad_ion_cloruro_model import permeabilidad_ion_cloruro_model
from schemas.other.id_str import all_register,id_str
from auth.jwt_bearer import jwtBearer

msg = Message()

permeabilidadIonCloruro = APIRouter(
    prefix='/api/permeabilidadIonCloruro',
    tags=['permeabilidadIonCloruro'],
    dependencies=[Depends(jwtBearer())]
)


@permeabilidadIonCloruro.get('/',name='permeabilidadIonCloruro',description='get all items',response_model=response_petition_model)
async def get_all_register():
    try:
        data = CrudFunctions.get_all_register('permeabilidadIonCloruro')
        result = all_register(data)
        return CustomMessage(200,msg.msg_get,result) 
    except:
        CustomMessage(400,'ocurrio un error')


@permeabilidadIonCloruro.get('/{id}',name='permeabilidadIonCloruro',description='get single item',response_model=response_petition_model)
def get_one_register(id:str):
    try:
        data = CrudFunctions.get_single_register('permeabilidadIonCloruro',id,where='permeabilidadIonCloruro')
        return CustomMessage(200,msg.msg_get,id_str(data))
    except:
        CustomMessage(400,'id no valido')

        
@permeabilidadIonCloruro.post('/',description='post item', name='post item',response_model=response_petition_model)
def post_regsiter(item:permeabilidad_ion_cloruro_model):
    try:
        id =  CrudFunctions.post_register('permeabilidadIonCloruro',item,True)
        return CustomMessage(201,msg.msg_add,{'_id':str(id)},'permeabilidadIonCloruro')
    except:
        CustomMessage(400,'id no valido')

@permeabilidadIonCloruro.put('/{id}',description='put item', name='put item',response_model=response_petition_model)
def put_register(id:str,body:permeabilidad_ion_cloruro_model):
    try:
        item  = CrudFunctions.put_register('permeabilidadIonCloruro',id,body,'permeabilidadIonCloruro')
        print('*************',item)
        return CustomMessage(200,msg.msg_update)
    except:
        CustomMessage(400,'ocurrio un error')



@permeabilidadIonCloruro.delete('/{id}',name='permeabilidadIonCloruro',description='delete item',response_model=response_petition_model)
def get_one_register(id:str):
    try:
        data = CrudFunctions.delete_register('permeabilidadIonCloruro',id,True,where='permeabilidadIonCloruro')
        if data > 0:
            return CustomMessage(200,msg.msg_delete)
        CustomMessage(400,'No su pudo eliminar')
    except:
        CustomMessage(400,'ocurrio un error')