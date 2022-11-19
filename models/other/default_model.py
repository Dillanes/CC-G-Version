from pydantic import BaseModel

class response_petition_model(BaseModel):
    detail:list = [{'data':'dict or list','msg':'str'}]