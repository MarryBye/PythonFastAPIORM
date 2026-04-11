from fastapi import Depends
from sqlalchemy import select, insert, delete, update
from utils.get_db_session import get_db_session

class UsersRepository:
    def __init__(self, db=Depends(get_db_session)):
        self.db = db

    async def get_user(self, user_id: int):
        query = select(User).where(User.id == user_id)
        result = await self.db.execute(query)
        return result.scalars().first()

    async def create_user(self, user_data: UserCreate):
        query = insert(User).values(**user_data.dict())
        await self.db.execute(query)

    async def update_user(self, user_id: int, user_data: UserUpdate):
        query = update(User).where(User.id == user_id).values(**user_data.dict())
        await self.db.execute(query)

    async def delete_user(self, user_id: int):
        query = delete(User).where(User.id == user_id)
        await self.db.execute(query)
