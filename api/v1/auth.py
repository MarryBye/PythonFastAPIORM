from fastapi import Depends
from fastapi.routing import APIRouter

from services.users import UsersService
from schemas.users import User, UserCreate, UserUpdate
from utils.get_db_session import get_db_session

router = APIRouter(prefix="/auth")