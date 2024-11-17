from fastapi import FastAPI
from contextlib import asynccontextmanager


# local imports
from src.database.connection import create_db_and_tables
from src.authentication.router import router as auth_router
from src.apps.profile.router import router as profile_router
from src.apps.communities.router import router as community_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # not needed if alembic was added
    print("\n----> [Server - up] ---->\n")
    await create_db_and_tables()
    yield
    print("\n<---- [Server - down] <----\n")


# a lifespan is logic is used to provide resources that are required throughout the application life tiem
# starts right at startup and ends after shutdown
app = FastAPI(lifespan=lifespan)
app.include_router(auth_router)
app.include_router(profile_router)
app.include_router(community_router)


@app.get('/')
async def index():
    return {"loc": "root"}


@app.get('/test')
async def test():
    return {'message': "Hello World test"}