def resistencia_concreto_schema(item)->dict:
    print('*****************',item)
    print('***********','clase' in item)
    
    return {
        '_id':str(item['_id']),
        'kgcm2': item['kgcm2'],
        'MPa':item['MPa'],
        'PSI':item['PSI'],
        'KSI':item['KSI'],
        'tipoResistencia':item['tipoResistencia'],
        'clase': 'clase' in item if item['clase'] else False
    }

def all_resistencia_concreto_schema(entity)->list:
    return [resistencia_concreto_schema(item) for item in entity]