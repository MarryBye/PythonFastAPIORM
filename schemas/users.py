from typing import Optional
from pydantic import *

class UserBase(BaseModel):
    login: str
    hashed_password: str
    firstname: str
    lastname: str
    nickname: str
    email: str

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    nickname: Optional[str] = None
    email: Optional[str] = None

class User(UserBase):
    id: int
    