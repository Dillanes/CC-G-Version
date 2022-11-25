from fastapi import APIRouter,status
from utils.customCrud import CrudFunctions
from utils.customMessages import CustomMessage
from models.userAuth.login_model import login_user
from auth.jwt_handler import token_response,singJWT,decodeJWT
from passlib.hash import pbkdf2_sha256

login = APIRouter(
    prefix='/api/login',
    tags=['login']
)

def check_user(body:login_user):
    user = CrudFunctions.get_single_register(nameDocument='empleado',id=None,register=body,where='Login')
    if user is None:
        CustomMessage(404,"email address doesn't exist on record",Where='Login',method='Post')
    new_body = dict(body)
    if user['email'] == new_body['email'] and pbkdf2_sha256.verify(new_body['password'],user['password']):
        return user
    return None
    
    




@login.post('/',status_code=status.HTTP_200_OK,name='Login User')
def login_user(body:login_user):
    res = check_user(body)
    if res is None:
        CustomMessage(401,'invalid credentials',Where='Login',method='Post')
    data = singJWT(res)
    return CustomMessage(200,detailMessagge='Ahutorizated',data=data,Where='Login',method='Post',)