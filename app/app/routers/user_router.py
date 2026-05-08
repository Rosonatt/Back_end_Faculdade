from fastapi import APIRouter
from app.schemas.user_schema import User
from app.services.user_service import *

router = APIRouter()
#GET/ALL Users
@router.get("/users")
def list_users():
    return get_all_users_service()

#POST - Create User
@router.post("/users")
def create_user(user: User):
    return create_user_service(user)

#GET - User by ID
@router.get("/users/{user_id}")
def get_user(user_id: str):
    return get_user_by_id_service(user_id)

#PUT - Update User
@router.put("/users/{user_id}")
def update_user(user_id: str, user: User):
    return update_user_service(user_id, user)

#DELETE - Delete User
@router.delete("/users/{user_id}")
def delete_user(user_id: str):
    return delete_user_service(user_id)