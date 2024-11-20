from typing import Optional
from sqlalchemy import Column, event, Enum
from sqlalchemy.dialects import postgresql
from sqlmodel import Field, SQLModel, Relationship
from datetime import datetime
from uuid import UUID, uuid4


from src.database.models.mixins import TimestampModel


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




class User(SQLModel, table=True):
    __tablename__ = 'users'
    id: int = Field(primary_key=True, index=True, nullable=False)
    email: str = Field(index=True, nullable=False, max_length=128)
    password: str = Field(nullable=False)
    is_active: bool = Field(default=False)
    vcode: str = Field(default=None)
    role: Optional[str] = Field(sa_column=Column("role", role_types, nullable=True))
    created_at: datetime = Field(sa_column=Column(postgresql.TIMESTAMP, default=datetime.now))
    updated_at: datetime = Field(sa_column=Column(postgresql.TIMESTAMP, default=datetime.now))

    # rename this to something other than dict() to be safe (making sure no conflict with internal methods)
    def get_dict_of_this(self):
        return {
            'id': self.id,
            'email': self.email,
            'vcode': self.vcode,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }