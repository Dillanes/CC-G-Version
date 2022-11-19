from dotenv import load_dotenv
from pydantic import BaseSettings
import os

#configurate initial of dotenv
load_dotenv()


#get all enviromen variables
class Settings(BaseSettings):
    HOST: str = os.getenv('HOST') #local host
    SECRET_KEY: str = os.getenv('SECRET_KEY')  
    ALGORITHM: str = os.getenv('ALGORITHM')  #algorithm of codification
    ACCESS_TOKEN_EXPIRE_MINUTES: str = os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')  
    PORT: str = os.getenv('PORT')  
    URI: str = os.getenv('URI')  #Url conection to mongo atlas
    SLACK_ERRORS: str = os.getenv('SLACK_ERRORS')  #Robot messages