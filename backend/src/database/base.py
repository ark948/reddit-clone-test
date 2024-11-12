from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, String, Integer




class Base(DeclarativeBase):
    pass



class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True, unique=True)
    msg = Column(String(10))