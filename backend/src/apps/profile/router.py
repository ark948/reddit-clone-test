# non-local imports
from fastapi import (
    APIRouter, Depends
)

# local imports
from src.database.connection import SessionDep
from src.authentication.users import current_active_user
from src.authentication.models import User, Profile
from src.apps.profile.schemas import CreateProfileSchema
from src.apps.profile import crud


router = APIRouter(prefix="/profile", tags=['Profile'])


# auth-required
@router.get('/get-profile')
def get_profile(user: User = Depends(current_active_user)):
    return {
        "user_id": user.id,
        "message": "Please complete your profile."
    }


@router.post('/create-profile')
async def create_profile(request: CreateProfileSchema, session: SessionDep, user: User=Depends(current_active_user)):
    try:
        await crud.create_profile(request=request, db=session, owner_id=user.id, owner=user)
    except Exception as error:
        return {"message": f"error: {error}"}
    return {"message": "OK"}