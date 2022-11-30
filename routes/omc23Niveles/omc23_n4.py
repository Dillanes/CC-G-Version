from config.messages import Message
from utils.customCrud import CrudFunctions
from utils.customMessages import CustomMessage
from fastapi import APIRouter,Depends
from models.other.default_model import response_petition_model
from models.omc23Niveles.omc23_model import omc23_model
from schemas.other.id_str import all_register,id_str
from auth.jwt_bearer import jwtBearer

msg = Message()

omniclasNivel4 = APIRouter(
    prefix='/api/omniclasNivel4',
    tags=['omniclasNiveles'],
    dependencies=[Depends(jwtBearer())]
)


@omniclasNivel4.get('/',name='omniclasNivel4',description='get all items',response_model=response_petition_model)
async def get_all_register():
    try:
        data = CrudFunctions.get_all_register('omniclass_level4')
        result = all_register(data)
        return CustomMessage(200,msg.msg_get,result) 
    except:
        CustomMessage(400,'ocurrio un error')


# @omniclasNivel4.get('/{id}',name='omniclasNivel4',description='get single item',response_model=response_petition_model)
# def get_one_register(id:str):
#     try:
#         data = CrudFunctions.get_single_register('omniclasNivel4',id,where='omniclasNivel4')
#         return CustomMessage(200,msg.msg_get,id_str(data))
#     except:
#         CustomMessage(400,'id no valido')

        
# @omniclasNivel4.post('/',description='post item', name='post item',response_model=response_petition_model)
# def post_regsiter(item:omc23_model):
#     try:
#         id =  CrudFunctions.post_register('omniclasNivel4',item,True)
#         return CustomMessage(201,msg.msg_add,{'_id':str(id)},'omniclasNivel4')
#     except:
#         CustomMessage(400,'id no valido')

# @omniclasNivel4.put('/{id}',description='put item', name='put item',response_model=response_petition_model)
# def put_register(id:str,body:omc23_model):
#     try:
#         item  = CrudFunctions.put_register('omniclasNivel4',id,body,'omniclasNivel4')
#         print('*************',item)
#         return CustomMessage(200,msg.msg_update)
#     except:
#         CustomMessage(400,'ocurrio un error')



# @omniclasNivel4.delete('/{id}',name='omniclasNivel4',description='delete item',response_model=response_petition_model)
# def get_one_register(id:str):
#     try:
#         data = CrudFunctions.delete_register('omniclasNivel4',id,True,where='omniclasNivel4')
#         if data > 0:
#             return CustomMessage(200,msg.msg_delete)
#         CustomMessage(400,'No su pudo eliminar')
#     except:
#         CustomMessage(400,'ocurrio un error')