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


# this is the old table (i don't know why this is wrong, did sqlalchemy docs changed over night?)
# profile_community_junction = Table(
#     'community_profile',
#     Base.metadata,
#     Column('profile_id', Integer, ForeignKey('profiles.id')),
#     Column('community_id', Integer, ForeignKey('communities.id')),
#     Column("created_at", DateTime, default=(datetime.now), nullable=False)
# )