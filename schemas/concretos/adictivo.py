def adictivo_schema(item)->dict:
    return {
        '_id':str(item['_id']),
        'adictivo': item['adictivo'],
        'tipoAdicitivo':item['tipoAdicitivo'],
        'aplicaciones':item['aplicaciones'],
        'comentario':item['comentario']
    }

def all_adictivo_schema(entity)->list:
    return [adictivo_schema(item) for item in entity]
