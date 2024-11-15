from sqlalchemy import Column, Integer, Table, ForeignKey, DateTime
from src.database.base import Base
from datetime import datetime


# create association tables here (also known as junction tables)

profile_community_junction = Table(
    'community_profile',
    Base.metadata,
    Column('profile_id', ForeignKey("profiles.id"), primary_key=True),
    Column('community_id', ForeignKey("communities.id"), primary_key=True),
)

# name is incorrect