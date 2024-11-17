import asyncio
import json
import os
from typing import Generator
from collections.abc import AsyncIterable

import pytest
import pytest_asyncio
from httpx import AsyncClient
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from src.database.base import Base
# from sqlmodel import SQLModel
# from sqlmodel.ext.asyncio.session import AsyncSession

from src.database.connection import engine as async_engine
from src import app




@pytest_asyncio.fixture(scope="function")
async def async_session() -> AsyncIterable[AsyncClient]:
   session = sessionmaker(
       async_engine, class_=AsyncSession, expire_on_commit=False
   )

   async with session() as se:
       async with async_engine.begin() as conn:
           await conn.run_sync(Base.metadata.create_all)
       yield se
   async with async_engine.begin() as conn:
       await conn.run_sync(Base.metadata.drop_all)
   await async_engine.dispose()



@pytest_asyncio.fixture
async def async_client():
   async with AsyncClient(
           app=app,
           base_url="http://127.0.0.1:8000"
   ) as client:
       yield client



@pytest.fixture(scope='session', name='evloop')
def event_loop():
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()
    yield loop
    loop.close()