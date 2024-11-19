# local imports
from src.authentication import schemas
from src.apps.auth.models import User
from src.authentication.hash import hash_plain_password
from src.authentication.utils import generateOtp
from src.database.dependencies import SessionDep

# other imports
from fastapi import HTTPException, status
from sqlmodel import select, Session

def get_all(session: SessionDep) -> list:
    statement = select(User)
    results = session.exec(statement).all()
    return results


def create(request: schemas.CreateUser, db: SessionDep) -> User:
    new_user = User(
            email=request.email,
            password=hash_plain_password(request.password),
        )
    new_user.vcode = generateOtp()
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def show(id: int, session: SessionDep) -> User:
    user = session.get(User, id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, from sqlmodel import SQLModel



class UpdateUserSQLModel(SQLModel):
    email: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    password: str | None = None
    is_active: bool | None = None
            detail=f"User with {id} was not found."
        )
    return user

def update(id: int, request: UpdateUserSQLModel, session: SessionDep) -> dict:
    db_user = session.get(User, id)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"User with {id} was not found."
        )
    user_data = request.model_dump(exclude_unset=True)
    db_user.sqlmodel_update(user_data)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return {"message": f"User with {id} updated."}
    

def delete(id: int, session: SessionDep) -> None:
    user = session.get(User, id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"User with {id} was not found."
        )
    session.delete(user)
    session.commit()
    return {"ok": True}


def get_user_from_email(email: str, session: SessionDep) -> User:
    statement = select(User).where(User.email == email)
    results = session.exec(statement)
    for user in results:
        if not user:
            raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"User with {email} was not found.")
        return user