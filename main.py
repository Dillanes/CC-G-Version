from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from routes import all_routes



#initial config, create app*********************
app =  FastAPI(
    title= "API CCG",
    description= "Desarrollo de apis para la aplicacion CCG",
    version='0.0.1',
    terms_of_service='http://example.com/terms/',
    contact= dict(
        name = "some contact",
        email = "some_email2@gmail.com"       
    ),
    license_info=dict(
        name="ORG 2.2",
        url = "https://www.apache.org/locense/LICENSE-2.0.html"
    ),
    openapi_url='/api/v1/openapi.json', #route for do open api in format json  
    docs_url="/docs", #route for docts
    redoc_url="/redoct", 

)

#middleaware for cross origins**************

#white list
origins = [
    "http://localhost:3000",
    "http://localhost:3001",
    "http://localhost",
    "http://localhost:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, #white list
    allow_credentials=True, 
    allow_methods=["*"], #accepts all http methods
    allow_headers=["*"], 
)


#GET ALL ROUTES****************

#rutes authUser
app.include_router(all_routes.userRegiter)
app.include_router(all_routes.login)


#RUTAS CONCRETO PREMEZCLADO
app.include_router(all_routes.concretoPremezclado)
app.include_router(all_routes.adictivo)
app.include_router(all_routes.edadResistencia)
app.include_router(all_routes.resistenciaConcreto)
app.include_router(all_routes.moduloElasticidad)
app.include_router(all_routes.densidadConcreto)
app.include_router(all_routes.contraccionSecado)
app.include_router(all_routes.fibra)
app.include_router(all_routes.TMA)
app.include_router(all_routes.revenimiento)
app.include_router(all_routes.agregado)
app.include_router(all_routes.colocacionConcreto)
app.include_router(all_routes.permeabilidadIonCloruro)
app.include_router(all_routes.claseExposicion)
app.include_router(all_routes.cemento)
app.include_router(all_routes.colorConcreto)


#configurate static files*******
app.mount('/static',StaticFiles(directory='static'),name='static')
