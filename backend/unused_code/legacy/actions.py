from src.database.connection import SessionDep
from src.apps.models import Profile
from src.apps.models import Community
from sqlalchemy import select
from sqlalchemy.orm import joinedload


# common actions such as joining a community are done here


async def profile_join_community(user_id: int, community_id: int, db: SessionDep) -> bool:
    result: bool = False

    try:
        query_result = await db.execute(
                select(Profile)
                .options(joinedload(Profile.joined))
                .where(Profile.owner_id==user_id)
            )
        profileObj =  query_result.scalar()
    except Exception as error:
        print("[1]\n\n", error, "\n\n")

    try:
        communityObj = await db.get(Community, community_id)
    except Exception as error:
        print("[2]\n\n", error, "\n\n")

    try:
        profileObj.joined.append(communityObj)
        db.add(profileObj)
        await db.commit()
        result = True
    except Exception as error:
        print("[3]\n\n", error, "\n\n")

    return result