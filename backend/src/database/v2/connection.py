from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated
from collections.abc import AsyncGenerator
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from src.config import DATABASE_URL
from src.database.base import Base
from sqlalchemy.orm import Session
from fastapi import Depends



engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)



async def create_db_and_tables():
    print("----> [Running create_db_and_tables.]\n")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)




async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    print("----> [Running get_async_session.]\n")
    async with async_session_maker() as session:
        yield session



SessionDep = Annotated[Session, Depends(get_async_session)]