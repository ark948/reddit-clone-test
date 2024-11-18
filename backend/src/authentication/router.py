from fastapi import APIRouter, Depends
from src.database.provider import get_session
from sqlalchemy.ext.asyncio.session import AsyncSession
from http import HTTPStatus


from src.authentication.dependencies import get_users_crud, UserServiceDep
from src.authentication.service import UsersCrud
from src.authentication.schemas import CreateUser, ShowUser
from src.database.dependencies import SessionDep
from src.database.models.sqlmodels import User
from typing import List


router = APIRouter(
    prefix='/auth'
)




@router.get('/')
async def index(session: AsyncSession=Depends(get_session)):
    pass


@router.get('/tset-get', response_model=ShowUser, status_code=HTTPStatus.OK)
async def get_user_by_repo(user_id: int, users: UsersCrud = Depends(get_users_crud), session: AsyncSession = Depends(get_session)):
    user = await users.get(user_id=user_id)


@router.post("/test-post", status_code=HTTPStatus.CREATED)
async def create_user_by_repo(data: CreateUser, users: UsersCrud = Depends(get_users_crud), session: AsyncSession = Depends(get_session)):
    user = await users.create(data=data)



@router.get('/get-user/{id}')
async def get_user_by_service(id: int, u: UserServiceDep):
    item = await u.get_user(id)
    return item



@router.get('/get-all-users', response_model=List[ShowUser])
async def get_all_users_by_service(users_service: UsersCrud = Depends(get_users_crud)):
    all_users = await users_service.get_all_users()
    return all_users


@router.post('/create-user', response_model=ShowUser, status_code=HTTPStatus.CREATED)
async def create_user_by_service(data: CreateUser, uesrs_service: UsersCrud = Depends(get_users_crud)):
    user = await uesrs_service.create_user(data=data)
    return user



@router.delete("/{user_id}")
async def delete_user(user_id):
    # status code http no content and return empty dict
    return {}