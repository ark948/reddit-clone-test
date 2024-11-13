from __future__ import annotations
from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.database.base import Base
from sqlalchemy import ForeignKey


from src.apps.profile.models import Profile

# teblename of User table from fastapi-users is 'user'
class User(SQLAlchemyBaseUserTableUUID, Base):
    profile_id: Mapped[int] = mapped_column(ForeignKey("profiles.id"))
    profile: Mapped["Profile"] = relationship(back_populates="owner")