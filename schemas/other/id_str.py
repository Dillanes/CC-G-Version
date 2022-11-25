def id_str(item):
        if item is None:
                return None
        item['_id'] = str(item['_id'])
        return item

def all_register(data)->list:
        if data is None:
                return []
        return [id_str(item) for item in data]