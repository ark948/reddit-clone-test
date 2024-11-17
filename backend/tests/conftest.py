import pytest
import pytest_asyncio
import uuid
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from fastapi.testclient import TestClient
from src import app
from src.database.base import Base
from src.database.connection import get_async_session



@pytest_asyncio.fixture(scope="function")
async def db_session():
    SQLITE_DATABASE_URL = "sqlite+aiosqlite:///./test_db.db"

    engine = create_async_engine(SQLITE_DATABASE_URL)
    TestingSessionLocal = async_sessionmaker(engine, autocommit=False, autoflush=False)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    connection = engine.connect()
    transaction = connection.begin()
    session = TestingSessionLocal(bind=connection)
    yield session
    session.close()
    transaction.rollback()
    connection.close()


@pytest_asyncio.fixture(scope="function", name='client')
def test_client(db_session):
    def override_get_db():
        try:
            yield db_session
        finally:
            db_session.close()

    app.dependency_overrides[get_async_session] = override_get_db
    with TestClient(app) as test_client:
        yield test_client
