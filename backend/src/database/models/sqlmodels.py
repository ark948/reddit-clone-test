from typing import Optional
from sqlalchemy import Column, event, Enum
from sqlalchemy.dialects import postgresql
from sqlmodel import Field, SQLModel, Relationship
from datetime import datetime
from uuid import UUID, uuid4


from src.database.models.mixins import TimestampModel, UUIDModel


role_prefix = 'user'
role_types = postgresql.ENUM(
    "member",
    "moderator",
    "admin",
    name=f'{role_prefix}_role'
)


# User -> Profile | Profile -> User (one-to-one)
# mixins are not used yet

@event.listens_for(SQLModel.metadata, "before_create")
def _create_enums(metadata, conn, **kw):
    role_types.create(conn, checkfirst=True)



class UserBase(SQLModel):
    email: str = Field(index=True, nullable=False, max_length=128)
    password: str
    is_active: bool = Field(default=False)
    role: Optional[str] = Field(sa_column=Column("role", role_types, nullable=True))


class User(UserBase, table=True):
    __tablename__ = 'users'
    id: int = Field(primary_key=True, index=True, nullable=False)
    vcode: str = Field(default=None)
    created_at: datetime = Field(
            sa_column=Column(postgresql.TIMESTAMP),
            default=datetime.now, nullable=False
        )
    updated_at: datetime = Field(
            sa_column=Column(postgresql.TIMESTAMP),
            default=datetime.now, nullable=False
        )
    profile: Optional["Profile"] = Relationship(back_populates="owner")

    def __repr__(self) -> str:
        return f'User -> {self.id}'

    def dict(self):
        return {
            'uid': self.id,
            'vcode': self.vcode,
            'profile': self.profile # may cause error
        }


class Profile(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    username: str = Field(unique=True, nullable=False, max_length=64)
    owner_id: int = Field(foreign_key='users.id')
    owner: User = Relationship(back_populates="profile")

    def __repr__(self) -> str:
        return f'Profile -> {self.username}'

    def dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'username': self.username,
            'owner_id': self.owner_id,
            'owner': self.owner # may cause error
        }