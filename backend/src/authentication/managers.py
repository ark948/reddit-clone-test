import uuid
from typing import Optional
from fastapi_users import UUIDIDMixin, BaseUserManager
from fastapi_users.db import SQLAlchemyUserDatabase
from fastapi import Request, Depends
from src.authentication.models import User
from src.config import SECRET_KEY
from src.authentication.db import get_user_db

from src.apps.profile.crud import create_profile
from src.database import context



class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    reset_password_token_secret = SECRET_KEY
    verification_token_secret = SECRET_KEY

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")

    async def on_after_forgot_password(self, user: User, token: str, request: Optional[Request] = None):
        print(f"User {user.id} has forgot their password. Reset token: {token}")

    async def on_after_request_verify(self, user: User, token: str, request: Optional[Request] = None):
        print(f"Verification requested for user {user.id}. Verification token: {token}")



async def get_user_manager(user_db: SQLAlchemyUserDatabase = Depends(get_user_db)):
    yield UserManager(user_db)