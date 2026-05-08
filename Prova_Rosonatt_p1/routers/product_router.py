from fastapi import APIRouter
from schemas.product_schema import Product
from services import product_service

router = APIRouter(prefix="/produtos", tags=["Produtos"])

@router.get("/")
def listar_produtos():
    return product_service.get_all_products()

@router.post("/", status_code=201)
def criar_produto(produto: Product):
    return product_service.create_product(produto)

@router.get("/{id}")
def buscar_produto(id: str):
    return product_service.get_product_by_id(id)

@router.put("/{id}")
def atualizar_produto(id: str, produto: Product):
    return product_service.update_product(id, produto)

@router.delete("/{id}")
def deletar_produto(id: str):
    return product_service.delete_product(id)