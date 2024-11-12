from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from sqlalchemy import Column, String
from src.database.base import Base




class User(SQLAlchemyBaseUserTableUUID, Base):
    first_name = Column(String(50), nullable=True)
    last_name = Column(String(50), nullable=True)
    username = Column(String(64), nullable=False, unique=True)