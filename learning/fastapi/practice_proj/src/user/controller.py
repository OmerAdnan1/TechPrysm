from src.user.dtos import UserSchema
from src.user.models import UserModel

from sqlalchemy.orm import Session
from fastapi import HTTPException

from pwdlib import PasswordHash


password_hash = PasswordHash.recommended()
def get_password_hash(password):
    return password_hash.hash(password)


def register(body:UserSchema, db:Session):

    #TODO
    ## 1. Username Validations
    is_user = db.query(UserModel).filter(UserModel.username == body.username).first()
    if is_user:
        raise HTTPException(status_code=400, detail="Username Already exists...")

    ## 2. Email Validations
    is_user = db.query(UserModel).filter(UserModel.email == body.email).first()
    if is_user:
        raise HTTPException(status_code=400, detail="Email already exists...")


    hash_password = get_password_hash(body.password)
    new_user = UserModel(
        name = body.name,
        email = body.email,
        hashed_password = hash_password,
        username = body.username
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user



