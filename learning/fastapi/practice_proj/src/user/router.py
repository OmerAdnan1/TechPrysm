from fastapi import APIRouter, Depends, status
from src.user.dtos import UserSchema, UserResponseSchema
from src.user import controller
from sqlalchemy.orm import Session
from src.utils.db import get_db

user_routes = APIRouter(prefix="/user")


@user_routes.post("/create_user")
def register(body: UserSchema, db:Session = Depends(get_db), status_code=status.HTTP_201_CREATED, return_model=UserResponseSchema):
    return controller.register(body, db)







