from __future__ import annotations

# non-local imports
from sqlalchemy import String, ForeignKey, Text
from sqlalchemy.orm import relationship, Mapped, mapped_column
from typing import List

# local imports
from src.database.base import Base
from src.apps.associations import profile_community_junction
from src.apps.mixins import Timestamp


# User --> Profile (one-to-one) (checked)
# Profile --> Community (many-to-many) (association table - checked)
# Profile --> Post (one-to-many) (checked)
# Profile --> Comment (one-to-many) (checked)
# Post --> Comment (one-to-many) (checked)
# Community --> Post (one-to-many) (checked)


class Profile(Timestamp, Base):
    __tablename__ = "profiles"
    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    username: Mapped[str] = mapped_column(String(64), unique=True, nullable=False)
    owner_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    owner: Mapped["User"] = relationship(back_populates="profile")
    joined: Mapped[List[Community]] = relationship(secondary=profile_community_junction, back_populates="members")
    posts: Mapped[List["Post"]] = relationship(back_populates="author", cascade="all, delete")
    comments: Mapped[List["Comment"]] = relationship(back_populates="author")
    stars: Mapped[int]
    # update stars --> mapped_column(nullable=True)



class Community(Timestamp, Base):
    __tablename__ = "communities"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(32))
    about: Mapped[str] = mapped_column(String(128))
    members: Mapped[List[Profile]] = relationship(secondary=profile_community_junction,back_populates="joined")
    posts: Mapped[List["Post"]] = relationship(back_populates="community")



class Post(Timestamp, Base):
    __tablename__ = 'posts'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(32))
    body: Mapped[str] = mapped_column(Text)
    author_id: Mapped[int] = mapped_column(ForeignKey("profiles.id", ondelete="CASCADE"))
    author: Mapped["Profile"] = relationship(back_populates="posts")
    community_id: Mapped[int] = mapped_column(ForeignKey('communities.id'))
    community: Mapped["Community"] = relationship(back_populates="posts")
    comments: Mapped[List["Comment"]] = relationship(back_populates="post")



class Comment(Timestamp, Base):
    __tablename__ = "comments"
    id: Mapped[int] = mapped_column(primary_key=True)
    body: Mapped[str] = mapped_column(String(256))
    author_id: Mapped[int] = mapped_column(ForeignKey("profiles.id"))
    author: Mapped["Profile"] = relationship(back_populates="comments")
    post_id: Mapped[int] = mapped_column(ForeignKey('posts.id'))
    post: Mapped["Post"] = relationship(back_populates="comments")




