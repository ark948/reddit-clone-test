# non-local imports
from fastapi import (
    APIRouter, Depends, status
)


# local imports
from src.apps.communities import crud
from src.authentication.models import User
from src.authentication.users import current_active_user
from src.apps.communities.schemas import CreateCommunitySchema
from src.database.connection import SessionDep


router = APIRouter(prefix="/community", tags=['Community'])


@router.get('/')
async def get_loc():
    return {"loc": "community index"}



@router.get('/get-community')
async def get_community(request: int, session: SessionDep, user: User=Depends(current_active_user)):
    obj = await crud.show_community_with_members(request=request, db=session)
    return obj



@router.post('/create-community')
async def create_community(request: CreateCommunitySchema, session: SessionDep, user: User = Depends(current_active_user)):
    obj = await crud.add_community(request=request, db=session)
    return obj
    