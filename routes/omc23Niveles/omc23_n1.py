from config.messages import Message
from utils.customCrud import CrudFunctions
from utils.customMessages import CustomMessage
from fastapi import APIRouter,Depends
from models.other.default_model import response_petition_model
from models.omc23Niveles.omc23_model import omc23_model
from schemas.other.id_str import all_register,id_str
from auth.jwt_bearer import jwtBearer

msg = Message()

omniclasNivel1 = APIRouter(
    prefix='/api/omniclasNivel1',
    tags=['omniclasNiveles'],
    dependencies=[Depends(jwtBearer())]
)


@omniclasNivel1.get('/',name='omniclasNivel1',description='get all items',response_model=response_petition_model)
async def get_all_register():
    try:
        data = CrudFunctions.get_all_register('omniclass_level1')
        result = all_register(data)
        return CustomMessage(200,msg.msg_get,result) 
    except:
        CustomMessage(400,'ocurrio un error')


# @omniclasNivel1.get('/{id}',name='omniclasNivel1',description='get single item',response_model=response_petition_model)
# def get_one_register(id:str):
#     try:
#         data = CrudFunctions.get_single_register('omniclasNivel1',id,where='omniclasNivel1')
#         return CustomMessage(200,msg.msg_get,id_str(data))
#     except:
#         CustomMessage(400,'id no valido')

        
# @omniclasNivel1.post('/',description='post item', name='post item',response_model=response_petition_model)
# def post_regsiter(item:omc23_model):
#     try:
#         id =  CrudFunctions.post_register('omniclasNivel1',item,True)
#         return CustomMessage(201,msg.msg_add,{'_id':str(id)},'omniclasNivel1')
#     except:
#         CustomMessage(400,'id no valido')

# @omniclasNivel1.put('/{id}',description='put item', name='put item',response_model=response_petition_model)
# def put_register(id:str,body:omc23_model):
#     try:
#         item  = CrudFunctions.put_register('omniclasNivel1',id,body,'omniclasNivel1')
#         print('*************',item)
#         return CustomMessage(200,msg.msg_update)
#     except:
#         CustomMessage(400,'ocurrio un error')



# @omniclasNivel1.delete('/{id}',name='omniclasNivel1',description='delete item',response_model=response_petition_model)
# def get_one_register(id:str):
#     try:
#         data = CrudFunctions.delete_register('omniclasNivel1',id,True,where='omniclasNivel1')
#         if data > 0:
#             return CustomMessage(200,msg.msg_delete)
#         CustomMessage(400,'No su pudo eliminar')
#     except:
#         CustomMessage(400,'ocurrio un error')