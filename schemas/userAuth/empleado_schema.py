def empleado_schema(item)->dict:
    return {
        '_id': str(item['_id']),
        'rfc': item['rfc'],
        'cargo':item['cargo'],
        'email':item['email'],
        'password':item['password'],
        'date_register':item['date_register'],
        'last_login':item['last_login'],
        'is_active':item['is_active'],
        'id_persona':item['id_per'],
        'id_departamento':item['id_departamento']
    }


def insert_empleado_schema(item)->dict:
    return {
        'rfc': item['rfc'],
        'cargo':item['cargo'],
        'email':item['email'],
        'password':item['password'],
        'date_register':item['date_register'],
        'last_login':item['last_login'],
        'is_active':item['is_active'],
        'id_persona':item['id_per'],
        'id_departamento':item['id_departamento']
    }



def all_empleado_schema(entity)->list:
    return [empleado_schema(item) for item in entity]