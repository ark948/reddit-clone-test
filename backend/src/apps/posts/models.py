from __future__ import annotations
from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from src.database.base import Base
from typing import List, Optional

from src.apps.mixins import Timestamp



class Post(Timestamp, Base):
    __tablename__ = 'posts'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(32))
    body: Mapped[str] = mapped_column(Text)
    author_id: Mapped[int] = mapped_column(ForeignKey("profiles.id"))
    author: Mapped["Profile"] = relationship(back_populates="posts")
    community_id: Mapped[int] = mapped_column(ForeignKey('communities.id'))
    community: Mapped["Community"] = relationship(back_populates="posts")
    comments: Mapped[List["Comment"]] = relationship(back_populates="post")
