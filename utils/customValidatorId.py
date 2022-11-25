from fastapi.encoders import jsonable_encoder
from .customCrud import CrudFunctions
from .customMessages import CustomMessage
from config.messages import Message

msg = Message()

#VALIDAR QUE EXISTAN LOS IDS DENTRO DE LA DB
def verify_register_id_exists(body):
    new_user = jsonable_encoder(body)
    val = new_user.keys()
    for item in val:
        if 'fk_' in item:
            nameD = item.split('_')[1]
            exist = CrudFunctions.get_single_register(nameD,new_user[item])
            if not exist:
                CustomMessage(404,f'{item} no existe un registro con este id')

    return new_user