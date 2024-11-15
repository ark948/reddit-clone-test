# non-local imports
from sqlalchemy import select
from sqlalchemy.orm import lazyload
from sqlalchemy.orm import joinedload

# local imports
from src.apps.models import Profile
from src.database.connection import SessionDep
from src.authentication.models import User
from src.apps.profile.schemas import (
    CreateProfileSchema,
)

# using eager loading (joinload)
async def read_profile_by_user(id: int, db: SessionDep) -> User:
    result = await db.execute(
        select(User)
        .options(joinedload(User.profile))
        .where(User.id == id)
    )
    return result.scalar()


# no longer works if profile has joined any community
async def read_profile(id: int, db: SessionDep) -> Profile:
    results = await db.execute(select(Profile).where(Profile.owner_id==id))
    return results.scalar()



async def read_profile_with_communities(id: int, db: SessionDep) -> Profile:
    result = await db.execute(
        select(Profile)
        .options(joinedload(Profile.joined))
    )
    return result.scalar()



async def create_profile(request: CreateProfileSchema, db: SessionDep, owner_id: int, owner: User
    ) -> Profile:
    profile_object = Profile(
        first_name=request.first_name,
        last_name=request.last_name,
        username=request.username,
        owner_id=owner_id,
        owner=owner,
        stars=0)
    
    db.add(profile_object)
    print("add - done")
    await db.commit()
    print("commit - done")
    await db.refresh(profile_object)
    print("refresh - done")
        
    return profile_object