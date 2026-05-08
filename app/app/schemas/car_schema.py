from pydantic import BaseModel

class Cars(BaseModel):
    modelo: str
    ano: str
    marca: str