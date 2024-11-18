from fastapi import APIRouter, Depends
from src.database.provider import get_session
from sqlalchemy.ext.asyncio.session import AsyncSession
from http import HTTPStatus


from src.authentication.dependencies import get_users_crud
from src.authentication.service import UsersCrud
from src.authentication.schemas import CreateUser, ShowUser


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


@router.get('/test-get-02')
async def get_user_by_service(data: CreateUser, session: AsyncSession = Depends(get_session)):
    book = await UsersCrud(session=session).create(data=data)


@router.delete("/{user_id}")
async def delete_user(user_id):
    # status code http no content and return empty dict
    return {}