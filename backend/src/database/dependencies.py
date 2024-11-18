from src.database.provider import get_session
from typing import Annotated
from sqlmodel.ext.asyncio.session import AsyncSession
from fastapi import Depends





SessionDep = Annotated[AsyncSession, Depends(get_session)]