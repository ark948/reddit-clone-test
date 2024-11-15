# non-local imports
from fastapi import (
    APIRouter, Depends, status
)

# local imports
from src.database.connection import SessionDep
from src.authentication.users import current_active_user
from src.authentication.models import User, Profile
from src.apps.profile.schemas import (
    CreateProfileSchema,
    ReadProfileSchema
)
from src.apps.profile import crud


router = APIRouter(prefix="/profile", tags=['Profile'])


# auth-required
@router.get('/get-loc')
async def get_loc(user: User = Depends(current_active_user)):
    return {
        "user_id": user.id,
        "message": "Please complete your profile if you haven't already."
    }


# this works without resposne_model (it returns User object with profile as child)
@router.get('/get-user-profile', status_code=status.HTTP_200_OK)
async def get_user_profile(session: SessionDep, user: User = Depends(current_active_user)):
    return await crud.read_profile_by_user(id=user.id, db=session)



@router.get('/get-profile', response_model=ReadProfileSchema, status_code=status.HTTP_200_OK)
async def get_profile(session: SessionDep, user: User = Depends(current_active_user)):
    return await crud.read_profile(id=user.id, db=session)



@router.post('/create-profile', status_code=status.HTTP_201_CREATED)
async def create_profile(request: CreateProfileSchema, session: SessionDep, user: User=Depends(current_active_user)):
    try:
        profileObject = await crud.create_profile(request=request, db=session, owner_id=user.id, owner=user)
    except Exception as error:
        return {"message": f"error: {error}"}
    return {
        "message": "OK",
        "profile_id": profileObject.id,
        "username": profileObject.username
    }