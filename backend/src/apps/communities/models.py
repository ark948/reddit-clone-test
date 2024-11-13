from __future__ import annotations
from sqlalchemy import String
from sqlalchemy.orm import relationship, Mapped, mapped_column

from typing import List

from src.database.base import Base
from src.apps.mixins import Timestamp

class Community(Timestamp, Base):
    __tablename__ = "communities"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(32))
    about: Mapped[str] = mapped_column(String(128))
    members: Mapped[List["Profile"]] = relationship(back_populates="joined")
    posts: Mapped[List["Post"]] = relationship(back_populates="community")