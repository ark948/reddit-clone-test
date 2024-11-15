# non-local imports
from sqlalchemy import select
from sqlalchemy.orm import joinedload


# local imports
from src.apps.models import Community
from src.database.connection import SessionDep
from src.apps.communities.schemas import CreateCommunitySchema


async def show_community(request: int, db: SessionDep):
    obj = await db.get(Community, request)
    return obj


async def show_community_with_members(request: int, db: SessionDep):
    result = await db.execute(
        select(Community)
        .options(joinedload(Community.members))
        .where(Community.id==request)
        )
    return result.scalar()



async def add_community(request: CreateCommunitySchema, db: SessionDep) -> Community:
    community_obj = Community(title=request.title, about=request.about)
    try:
        db.add(community_obj)
        await db.commit()
        await db.refresh(community_obj)
    except Exception as error:
        print("ERROR")
        return "error"
    return community_obj
