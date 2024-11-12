from fastapi import Depends
from src.authentication.models import User
from sqlalchemy.ext.asyncio import AsyncSession
from src.database.connection import get_async_session
from fastapi_users.db import SQLAlchemyUserDatabase


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)
