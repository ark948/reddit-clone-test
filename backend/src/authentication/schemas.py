from pydantic import BaseModel, ConfigDict, EmailStr
from typing import Optional

# EmailStr --> pip install email-validator


class ShowUser(BaseModel):
    id: int
    email: EmailStr
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    is_active: bool = False
    vcode: str
    model_config = ConfigDict(form_attributes=True, json_schema_extra={
        "example": {
            "email" : "some@some.com",
            # and the rest...
        }
    })


class CreateUser(BaseModel):
    email: EmailStr
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    password: str
    is_active: bool = False
    model_config = ConfigDict(form_attributes=True)


class VerifyUser(BaseModel):
    vcode: str



class ForgetPasswordRequest(BaseModel):
    email: EmailStr


class SuccessMessage(BaseModel):
    success: bool
    status_code: int
    message: str


class SetNewPassword(BaseModel):
    secret_token: str
    new_password: str
    confirm_password: str