from pymongo import MongoClient

#conexion local in default
conexion = MongoClient('mongodb+srv://consulting:C&C*20221@clusterbases.f92n1fx.mongodb.net/test')

#get db azureCorregida
conn = conexion.productosSeparados

conectdb = conexion