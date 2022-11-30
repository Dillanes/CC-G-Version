from pymongo import MongoClient
from config.config_env import Settings

env_var =  Settings()
#conexion local in default
conexion = MongoClient(env_var.URI)

#get db azureCorregida
conn = conexion.productosSeparados

conectdb = conexion