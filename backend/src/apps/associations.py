from sqlalchemy import Column, Integer, Table, ForeignKey, DateTime
from src.database.base import Base
from datetime import datetime


# create association tables here (also known as junction tables)


# profile --> community
# community --> profile
profile_community_junction = Table(
    'community_profile',
    Base.metadata,
    Column('profile_id', Integer, ForeignKey('profiles.id')),
    Column('community_id', Integer, ForeignKey('communities.id')),
    Column("created_at", DateTime, default=(datetime.now), nullable=False)
)