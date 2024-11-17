import asyncio
from httpx import AsyncClient
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from fastapi import FastAPI
import pytest_asyncio
import pytest

from src import app
from src.database.base import Base
from src.authentication.models import User
from src.database.connection import get_async_session
from src.authentication.hash import hash_plain_password


async_engine = create_async_engine(
    url='sqlite+aiosqlite://',
    echo=True,
)



# drop all database every time when test complete
@pytest_asyncio.fixture(scope='session')
async def async_db_engine():
    async with async_engine.begin(Base.metadata.create_all) as conn:
        await conn.run_sync()

    yield async_engine

    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)




# truncate all table to isolate tests
@pytest_asyncio.fixture(scope='function')
async def async_db(async_db_engine):
    async_session = sessionmaker(
            expire_on_commit=False,
            autocommit=False,
            autoflush=False,
            bind=async_db_engine,
            class_=AsyncSession,
        )
    async with async_session() as session:
        await session.begin()

        yield session

        await session.rollback()


@pytest_asyncio.fixture(scope='function', name="client")
async def async_client(async_db):

    def override_get_db():
        try:
            yield async_db
        finally:
            async_db.close()

    app.dependency_overrides[get_async_session] = override_get_db
    async with AsyncClient(app=app, base_url='http://127.0.0.1:8000') as async_client:
        yield async_client
    app.dependency_overrides.clear()



# let test session to know it is running inside event loop
@pytest.fixture(scope='session', name='evloop')
def event_loop():
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()
    yield loop
    loop.close()



# assume we have a example model
@pytest_asyncio.fixture(name='user')
async def async_user_orm(async_db) -> User:
    user = User(email='test@test.com', hashed_password=hash_plain_password('123'))
    async_db.add(user)
    await async_db.commit()
    await async_db.refresh(user)
    return user
