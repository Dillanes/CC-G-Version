from fastapi import HTTPException,status
from config.config_env import Settings
import requests
from datetime import datetime


settings = Settings()

def CustomMessage(
    resiveStatus:int=200,
    detailMessagge:str='msg',
    data:list or dict = None,
    Where:str='somewhere',
    user:str='someone',
    method:str='get'):

    
    URL = settings.SLACK_ERRORS   #URI SLACK
    MSG = f'Detalle:{detailMessagge}, Ruta: {Where}, User:{user}, Method:{method}, date:{datetime.now()}' #set info
    requests.post(URL,json={'text':MSG}) #send message to slack robot 

    #Otions tipe messages
    if resiveStatus == 404:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=[{'msg':detailMessagge,'data':data}])

    if resiveStatus == 400:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=[{'msg':detailMessagge,'data':data}])

    if resiveStatus == 401:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=[{'msg':detailMessagge,'data':data}])

    if resiveStatus == 200 or 201:
        return {'detail':[{'msg':detailMessagge,'data':data}]}
    