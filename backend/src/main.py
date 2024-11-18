from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.database.provider import init_db


from src.authentication.router import router as auth_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # not needed if alembic was added
    print("\n----> [Server - up] ---->\n")
    await init_db()
    yield
    print("\n<---- [Server - down] <----\n")



app = FastAPI(
        title="Reddit Clone",
        version="0.1.0",
        description="A simple clone of reddit using FastAPI",
        lifespan=lifespan
    )

app.include_router(auth_router)

@app.get('/')
async def index():
    return {"loc": "root"}


@app.get('/test')
async def test():
    return {'message': "Hello World test"}