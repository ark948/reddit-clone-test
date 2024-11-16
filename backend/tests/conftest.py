import pytest
from sqlalchemy.pool import StaticPool
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import DeclarativeBase
from fastapi.testclient import (
    TestClient
)

# import main app, models and get_session
from src import app
from src.database.connection import get_async_session
from src.database.base import Base



# fixtures

@pytest.fixture(name='session')
def session_fixture():
    engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool
    )
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        yield session


@pytest.fixture(name='client')
def client_fixture(session: Session):
    def get_session_override():
        return session
    
    app.dependency_overrides[get_async_session] = get_session_override
    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()

# in actual tests, session fixture must come before client fixture