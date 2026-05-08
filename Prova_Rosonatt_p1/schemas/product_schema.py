from pydantic import BaseModel

class Product(BaseModel):
    nome:str
    preço:float
    quantidade:int