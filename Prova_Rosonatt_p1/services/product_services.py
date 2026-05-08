from bson import ObjectId
from bson.errors import InvalidId
from fastapi import HTTPException
from repositories import product_repository
from schemas.product_schema import Product

def _validar_id(id: str) -> ObjectId:
    try:
        return ObjectId(id)
    except InvalidId:
        raise HTTPException(status_code=400, detail="ID mão encontrado")

def create_product(produto: Product):
    novo_produto = produto.model_dump()
    resultado = product_repository.create_product(novo_produto)
    return {"mensagem": "Produto criado", "id": str(resultado.inserted_id)}

def get_all_products():
    produtos = product_repository.get_all_products()
    lista_formatada = []
    for p in produtos:
        p["_id"] = str(p["_id"])
        lista_formatada.append(p)
    return lista_formatada

def get_product_by_id(id: str):
    obj_id = _validar_id(id)
    produto = product_repository.get_product_by_id(obj_id)
    
    if not produto:
        raise HTTPException(status_code=404, detail="Não achei o produto")
        
    produto["_id"] = str(produto["_id"])
    return produto

def update_product(id: str, produto: Product):
    obj_id = _validar_id(id)
    resultado = product_repository.update_product(obj_id, produto.model_dump())
    
    if resultado.matched_count == 0:
        raise HTTPException(status_code=404, detail="Não achei o produto")
        
    return {"mensagem": "Produto atualizado certinho"}

def delete_product(id: str):
    obj_id = _validar_id(id)
    resultado = product_repository.delete_product(obj_id)
    
    if resultado.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Não achei o produto")
        
    return {"mensagem": "Produto foi excluido"}