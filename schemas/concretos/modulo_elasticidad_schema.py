def modulo_elasticidad_schema(item)->dict:
    return {
        '_id':str(item['_id']),
        'kgcm2': item['kgcm2'],
        'MPa':item['MPa'],
        'PSI':item['PSI'],
    }