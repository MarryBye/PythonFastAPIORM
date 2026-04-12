from fastapi import Depends
from sqlalchemy import select, insert, delete, update
from alchemy.models.users import users
from schemas.users import UserCreate, UserUpdate, User
from utils.get_db_session import get_db_session

class UsersRepository:
    def __init__(self, db=Depends(get_db_session)):
        self.db = db

    async def get_users(self) -> list[User]:
        query = select(users)
        result = await self.db.execute(query)
        return result.mappings().all()

    async def get_user(self, user_id: int) -> User | None:
        query = select(users).where(users.columns.id == user_id)
        result = await self.db.execute(query)
        return result.mappings().first()

    async def create_user(self, user_data: UserCreate):
        query = insert(users).values(**user_data.model_dump())
        await self.db.execute(query)
        await self.db.commit()

    async def update_user(self, user_id: int, user_data: UserUpdate):
        query = update(users).where(users.columns.id == user_id).values(**user_data.model_dump(exclude_unset=True))
        await self.db.execute(query)
        await self.db.commit()

    async def delete_user(self, user_id: int):
        query = delete(users).where(users.columns.id == user_id)
        await self.db.execute(query)
        await self.db.commit()  
