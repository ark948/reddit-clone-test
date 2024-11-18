from sqlmodel import SQLModel, Field, Column
from sqlalchemy.dialects import postgresql
from uuid import uuid4, UUID
from sqlalchemy import text
from datetime import datetime






class UUIDModel(SQLModel): # do not use until sure
   uuid: UUID = Field(
       default_factory=uuid4,
       primary_key=True,
       nullable=False,
       sa_column_kwargs={
           "server_default": text("gen_random_uuid()"),
           "unique": True
       }
   )




class TimestampModel(SQLModel): # do not use until sure
   created_at: datetime = Field(
       default_factory=datetime.now,
       nullable=False,
       sa_column_kwargs={
           "server_default": text("current_timestamp(0)")
       }
   )

   updated_at: datetime = Field(
       default_factory=datetime.now,
       nullable=False,
       sa_column_kwargs={
           "server_default": text("current_timestamp(0)"),
           "onupdate": text("current_timestamp(0)")
       }
   )


class SampleUUIDModel(SQLModel):
       uid: UUID = Field(
        sa_column=Column(postgresql.UUID, primary_key=True, unique=True, default=uuid4)
    )