from pydantic import BaseModel, ConfigDict, EmailStr
from typing import Optional, List
from datetime import datetime
from src.database.models.sqlmodels import User


class CreateUser(BaseModel):
    email: str
    password: str
    model_config = ConfigDict(form_attributes=True)


class ShowUser(BaseModel):
    email: str
    model_config = ConfigDict(form_attributes=True)



class UserResponseModel(User):
    pass