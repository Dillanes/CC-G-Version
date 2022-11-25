def edad_resistencia_schema(item)->dict:
    return {
        '_id':str(item['_id']),
        'dias': item['dias'],
        'descripcion': item['descripcion']
    }


def all_edad_resistencia_schema(entity)->list:
    return [edad_resistencia_schema(item) for item in entity]
