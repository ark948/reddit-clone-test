from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import text
from src.settings import settings




async_engine = create_async_engine(url=settings.DATABASE_URL)



async def init_db():
    async with async_engine.begin() as conn:
        from src.database.models.sqlmodels import User
        from src.database.models.sqlmodels import Profile
        await conn.run_sync(SQLModel.metadata.create_all)