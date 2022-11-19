def insert_colonia_schema(item)->dict:
    return {
        'colonia':item['nombre_col'],
        'calle':item['calle'],
        'no_int':item['no_int'],
        'no_ext':item['no_ext'],
        'id_cp':item['id_cp']
    }

def colonia_schema(item)->dict:
    return {
        '_id':item['_id'],
        'colonia':item['nombre_col'],
        'calle':item['calle'],
        'no_int':item['no_int'],
        'no_ext':item['no_ext'],
        'id_cp':item['id_cp']
    }

def all_colonia_schema(entity)->list:
    return [colonia_schema(item) for item in entity]