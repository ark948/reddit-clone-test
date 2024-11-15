# non-local imports
from sqlalchemy import select



# local imports
from src.apps.models import Community
from src.database.connection import SessionDep
from src.apps.communities.schemas import CreateCommunitySchema



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
