from fastapi import Depends
from schemas.users import UserCreate, UserUpdate, User
from repositories.users import UsersRepository

class UsersService:
    def __init__(self, repo: UsersRepository = Depends()):
        self.repo = repo

    async def list_users(self) -> list[User]:
        return await self.repo.get_users()

    async def get_user(self, user_id: int) -> User | None:
        return await self.repo.get_user(user_id)

    async def create_user(self, user_data: UserCreate):
        await self.repo.create_user(user_data)

    async def update_user(self, user_id: int, user_data: UserUpdate):
        await self.repo.update_user(user_id, user_data)

    async def delete_user(self, user_id: int):
        await self.repo.delete_user(user_id)
