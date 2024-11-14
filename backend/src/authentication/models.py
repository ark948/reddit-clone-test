from __future__ import annotations
from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.database.base import Base
from sqlalchemy import ForeignKey


from src.apps.models import Profile

# teblename of User table from fastapi-users is 'user'
class User(SQLAlchemyBaseUserTableUUID, Base):
    profile: Mapped["Profile"] = relationship(back_populates="owner")