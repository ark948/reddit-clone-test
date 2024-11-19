from uuid import UUID

from fastapi import HTTPException
from fastapi import status as http_status
from sqlalchemy import delete, select
from sqlmodel.ext.asyncio.session import AsyncSession
from src.authentication import schemas
from src.database.models.sqlmodels import User
from src.authentication.hash import hash_plain_password
from src.authentication.utils import generateOtp
from typing import List


from src.database.dependencies import SessionDep

# init won't be async


class UsersCrud:
    def __init__(self, session: SessionDep) -> None:
        self.session = session

    
    async def get_all_users(self):
        stmt = select(User).order_by(User.created_at)
        result = await self.session.exec(statement=stmt)
        return result.all()


    async def get_user(self, user_id):
        stmt = select(User).where(User.id==user_id)
        result = await self.session.exec(statement=stmt)
        return result.first()



    async def create_user(self, new_user_data: schemas.CreateUser) -> User:
        new_user = User(email=new_user_data.email, password=hash_plain_password(new_user_data.password), vcode=generateOtp())
        self.session.add(new_user)
        await self.session.commit()
        await self.session.refresh(new_user)
        return new_user