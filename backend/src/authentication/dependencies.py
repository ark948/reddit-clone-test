from src.authentication.service import UsersCrud
from fastapi import Depends
from src.database.provider import get_session
from sqlalchemy.ext.asyncio.session import AsyncSession




async def get_users_crud(session: AsyncSession = Depends(get_session)) -> UsersCrud:
    return UsersCrud(session=session)


# SessionDep