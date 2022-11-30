from config.messages import Message
from utils.customCrud import CrudFunctions
from utils.customMessages import CustomMessage
from fastapi import APIRouter,Depends
from models.other.default_model import response_petition_model
from models.concretos.colocacion_model import colocacion_model
from schemas.other.id_str import all_register,id_str
from auth.jwt_bearer import jwtBearer

msg = Message()

resistenciaCompresion = APIRouter(
    prefix='/api/resistenciaCompresion',
    tags=['resistenciaCompresion'],
    dependencies=[Depends(jwtBearer())]
)


@resistenciaCompresion.get('/',name='resistenciaCompresion',description='get all items',response_model=response_petition_model)
async def get_all_register():
    try:
        data = CrudFunctions.get_all_register('23_13311300000000_02')
        result = all_register(data)
        return CustomMessage(200,msg.msg_get,result) 
    except:
        CustomMessage(400,'ocurrio un error')


# @resistenciaCompresion.get('/{id}',name='resistenciaCompresion',description='get single item',response_model=response_petition_model)
# def get_one_register(id:str):
#     try:
#         data = CrudFunctions.get_single_register('resistenciaCompresion',id,where='resistenciaCompresion')
#         return CustomMessage(200,msg.msg_get,id_str(data))
#     except:
#         CustomMessage(400,'id no valido')

        
# @resistenciaCompresion.post('/',description='post item', name='post item',response_model=response_petition_model)
# def post_regsiter(item:colocacion_model):
#     try:
#         id =  CrudFunctions.post_register('resistenciaCompresion',item,True)
#         return CustomMessage(201,msg.msg_add,{'_id':str(id)},'resistenciaCompresion')
#     except:
#         CustomMessage(400,'id no valido')

# @resistenciaCompresion.put('/{id}',description='put item', name='put item',response_model=response_petition_model)
# def put_register(id:str,body:colocacion_model):
#     try:
#         item  = CrudFunctions.put_register('resistenciaCompresion',id,body,'resistenciaCompresion')
#         print('*************',item)
#         return CustomMessage(200,msg.msg_update)
#     except:
#         CustomMessage(400,'ocurrio un error')



# @resistenciaCompresion.delete('/{id}',name='resistenciaCompresion',description='delete item',response_model=response_petition_model)
# def get_one_register(id:str):
#     try:
#         data = CrudFunctions.delete_register('resistenciaCompresion',id,True,where='resistenciaCompresion')
#         if data > 0:
#             return CustomMessage(200,msg.msg_delete)
#         CustomMessage(400,'No su pudo eliminar')
#     except:
#         CustomMessage(400,'ocurrio un error')