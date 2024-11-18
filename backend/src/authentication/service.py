from uuid import UUID

from fastapi import HTTPException
from fastapi import status as http_status
from sqlalchemy import delete, select
from sqlmodel.ext.asyncio.session import AsyncSession
from src.authentication.schemas import CreateUser
from src.database.models.sqlmodels import User


# init won't be async


class UsersCrud:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session


    async def create(self, data: CreateUser):
        new_user = User(**data.model_dump())
        # add self.session.add()
        # commit


    async def update_user(self, user_id: int, update_data: CreateUser):
        stmt = select(User).where(User.id == user_id)
        user = await self.session.exec(statement=stmt).first()
        for key, value in update_data.model_dump().items():
            setattr(user, key, value)
        await self.session.commit()
        