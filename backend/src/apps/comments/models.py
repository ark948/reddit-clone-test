from __future__ import annotations
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from src.database.base import Base


from src.apps.mixins import Timestamp


class Comment(Timestamp, Base):
    __tablename__ = "comments"
    id: Mapped[int] = mapped_column(primary_key=True)
    body: Mapped[str] = mapped_column(String(256))
    author_id: Mapped[int] = mapped_column(ForeignKey("profiles.id"))
    author: Mapped["Profile"] = relationship(back_populates="posts")
    post_id: Mapped[int] = mapped_column(ForeignKey('posts.id'))
    post: Mapped["Post"] = relationship(back_populates="comments")
