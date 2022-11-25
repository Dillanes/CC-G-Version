
def createStringIds(body):
    val = body.keys()
    result = ""
    for item in val:
        if 'fk_' in item:
            result = result + body[item]
    return result