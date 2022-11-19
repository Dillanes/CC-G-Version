from pydantic import BaseSettings

#default messages
class Message(BaseSettings):
    msg_error_add:str= "No se pudo agregar el registro"
    msg_error_update:str = 'No se pudo actualizar el registro'
    msg_error_delete:str = "No se pudo eliminar el registro"
    msg_delete:str = 'Registro eliminado'
    msg_add:str = 'Registro guardado'
    msg_get:str = 'Datos enviados'
    msg_error_dafault:str = 'ha ocurrido un error contacta con el administrador: CC&G@consultin.construction'
    msg_update:str = "Registro modificado"
    msg_idInvalid:str = 'El id no es valido'



# class Message(BaseSettings):
#     msg_error_add:str= "No se pudo agregar el registro"
#     msg_error_update:str = 'No se pudo actualizar el registro'
#     msg_error_delete:str = "No se pudo eliminar el"
#     msg_delete:str = 'the article has been deleted'
#     msg_add:str = 'item was been saved'
#     msg_get:str = 'Data sent'
#     msg_error_dafault:str = 'An error has occurred,send email israeldillanes2@gmail.com'
#     msg_update:str = "the article has been modified"
#     msg_idInvalid:str = 'The Id is invalid'