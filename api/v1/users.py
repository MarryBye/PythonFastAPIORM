from fastapi import Depends
from fastapi.routing import APIRouter

from services.users import UsersService
from schemas.users import User, UserCreate, UserUpdate
from utils.get_db_session import get_db_session

router = APIRouter(prefix="/users")

@router.get("/")
async def list_users(service: UsersService = Depends()):
    return {"users": await service.list_users()}

@router.get("/{user_id}")
async def get_user(user_id: int, service: UsersService = Depends()):
    user = await service.get_user(user_id)
    return {"user": user}

@router.post("/")
async def create_user(data: UserCreate, service: UsersService = Depends()):
    return {"user": await service.create_user(data)}

@router.put("/{user_id}")
async def update_user(user_id: int, data: UserUpdate, service: UsersService = Depends()):
    return {"user_id": user_id, "user": await service.update_user(user_id, data)}

@router.patch("/{user_id}")
async def partial_update_user(user_id: int, data: UserUpdate, service: UsersService = Depends()):
    return {"user_id": user_id, "user": await service.update_user(user_id, data)}

@router.delete("/{user_id}")
async def delete_user(user_id: int, service: UsersService = Depends()):
    await service.delete_user(user_id)
    return {"user_id": user_id}