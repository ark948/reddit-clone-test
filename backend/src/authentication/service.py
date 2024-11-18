from uuid import UUID

from fastapi import HTTPException
from fastapi import status as http_status
from sqlalchemy import delete, select
from sqlmodel.ext.asyncio.session import AsyncSession
from src.authentication.schemas import CreateUser, ShowUser
from src.database.models.sqlmodels import User
from src.authentication.hash import hash_plain_password
from src.authentication.utils import generateOtp
from typing import List


# init won't be async


class UsersCrud:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    
    async def get_all_users(self):
        stmt = select(User).order_by(User.created_at)
        result = await self.session.exec(statement=stmt)
        return result.all()


    async def get_user(self, id) -> User:
        result = await self.session.get(User, id)
        return result



    async def create_user(self, data: CreateUser) -> User:
        new_user = User(**data.model_dump())
        new_user.password = hash_plain_password(data.password)
        new_user.vcode = generateOtp()
        self.session.add(new_user)
        await self.session.commit()
        return new_user



    async def update_user(self, user_id: int, update_data: CreateUser):
        stmt = select(User).where(User.id == user_id)
        user = await self.session.exec(statement=stmt).first()
        for key, value in update_data.model_dump().items():
            setattr(user, key, value)
        await self.session.commit()
        