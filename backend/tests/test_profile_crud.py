from sqlalchemy import select
from src.apps.models import Profile
from src.authentication.models import User
from src.authentication.schemas import UserCreate
from src.authentication.managers import get_user_manager
from src.apps.profile.crud import (
    create_profile,
    read_profile_by_user,
    read_profile,
    read_profile_with_communities
)


def test_profile_table_is_empty(session):
    stmt = select(Profile)
    results = session.execute(statement=stmt).all()
    assert results == []

    

def test_user_create(session):
    user = User()
    print(user)