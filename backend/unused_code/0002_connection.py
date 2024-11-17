from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from collections.abc import AsyncGenerator
from sqlalchemy.orm import sessionmaker
from src.config import DATABASE_URL
from fastapi import APIRouter, Depends
from sqlalchemy import select, update


# create db connection
engine = create_async_engine(
    url=DATABASE_URL,
    echo=True,
)

async_session_global = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_global.begin() as session:
        try:
            yield session
        except:
            await session.rollback()
            raise
        finally:
            await session.close()




router = APIRouter()
@router.get('/api/async-examples/{id}')
async def get_example(id: int, db = Depends(get_async_session)):
    return await db.execute(select("SOMETHING")).all()

@router.put('/api/async-examples/{id}')
async def put_example(id: int, db = Depends(get_async_session)):
    await db.execute(update("SOMETHING").where(id=id).values(name='testtest', age=123))
    await db.commit()
    await db.refresh("SOMETHING")
    return await db.execute(select("SOMETHING").filter_by(id=id)).scalar_one()