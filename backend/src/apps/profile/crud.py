# local imports
from src.apps.models import Profile
from src.database.connection import SessionDep
from src.authentication.models import User
from src.apps.profile.schemas import CreateProfileSchema




async def create_profile(request: CreateProfileSchema, db: SessionDep, owner_id: int, owner: User
    ) -> Profile:
    profile_object = Profile(
        first_name=request.firstname,
        last_name=request.lastname,
        username=request.username,
        owner_id=owner_id,
        owner=owner,
        stars=0
        )
    
    db.add(profile_object)
    print("add - done")
    await db.commit()
    print("commit - done")
    await db.refresh(profile_object)
    print("refresh - done")
        
    return profile_object