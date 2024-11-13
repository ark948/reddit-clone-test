from __future__ import annotations
from src.database.base import Base
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from src.apps.associations import profile_community_junction

from typing import List
from src.apps.mixins import Timestamp



class Profile(Timestamp, Base):
    __tablename__ = "profiles"
    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    username: Mapped[str] = mapped_column(String(64), unique=True, nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    owner: Mapped["User"] = relationship(back_populates="profile")
    joined: Mapped[List["Community"]] = relationship(secondary=profile_community_junction, back_populates="members")
    posts: Mapped[List["Post"]] = relationship(back_populates="author")
    comments: Mapped[List["Comment"]] = relationship(back_populates="author")
    stars: Mapped[int]
    
    