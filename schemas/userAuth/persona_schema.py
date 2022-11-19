
def persona_schema(item)->dict:
    return {
        '_id':str(item['_id']),
        'nombre':item['nombre'],
        'apellido_p':item['apellido_p'],
        'apellido_m':item['apellido_m'],
        'genero':item['genero'],
        'fecha_nacimiento':item['fecha_nacimiento'],
        'tel':item['tel'],
        'curp':item['curp'],
        'id_col':item['id_col']
    }


def all_person_schema(entity)->list:
    return [persona_schema(item) for item in entity]



def insert_persona_schema(item)->dict:
    return {
        'nombre':item['nombre'],
        'apellido_p':item['apellido_p'],
        'apellido_m':item['apellido_m'],
        'genero':item['genero'],
        'fecha_nacimiento':item['fecha_nacimiento'],
        'tel':item['tel'],
        'curp':item['curp']
    }