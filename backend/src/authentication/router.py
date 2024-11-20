from fastapi import APIRouter, Depends
from src.database.provider import get_session
from sqlalchemy.ext.asyncio.session import AsyncSession
from http import HTTPStatus
from fastapi.responses import JSONResponse


from src.authentication.dependencies import get_users_crud, UserServiceDep
from src.authentication.service import UsersCrud
from src.authentication.schemas import UserResponseModel
from src.authentication import schemas
from src.database.dependencies import SessionDep
from src.database.models.sqlmodels import User
from typing import List, Dict

from sqlmodel import select


router = APIRouter(
    prefix='/auth'
)



@router.post('/create-user', status_code=HTTPStatus.CREATED)
async def create_user_by_service(u: UserServiceDep, data: schemas.CreateUser):
    user = await u.create_user(new_user_data=data)
    return user



@router.get('/get-user/{id}')
async def get_user_by_service(given_id: int, u: UserServiceDep):
    result = await u.get_user(user_id=given_id)
    if result:
        return result[0]
    return {"result": "no user found."}
    

# this works
@router.get('/get-all')
async def get_all_users(session: SessionDep):
    stmt = select(User).order_by(User.created_at)
    results = await session.exec(statement=stmt)
    return results.all()


# also ok
@router.get('/get-all2', response_model=List[UserResponseModel])
async def get_all_users2(session: SessionDep):
    results = await UsersCrud(session=session).get_all_users()
    data = []
    for user in results:
        data.append(user[0])
    return data


# also ok
@router.get('/get-all3', response_model=List[UserResponseModel], status_code=HTTPStatus.OK)
async def get_all_users3(u: UserServiceDep):
    results = await u.get_all_users()
    data = []
    for user in results:
        data.append(user[0])
    return data