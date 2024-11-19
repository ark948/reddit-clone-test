from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlmodel import text
from src.settings import settings




async_engine = create_async_engine(url=settings.DATABASE_URL)



async def init_db():
    async with async_engine.begin() as conn:
        from src.database.models.sqlmodels import User
        await conn.run_sync(SQLModel.metadata.create_all)




async def get_session() -> AsyncSession:
    async_sessoin = sessionmaker(
        bind=async_engine,
        class_=AsyncSession,
        expire_on_commit=False # do not expire session after committing
    )

    async with async_sessoin() as sesion:
        yield sesion