from typing import Annotated

from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from src.auth import controller
from src.auth.dtos import TokenSchema
from src.user.dtos import UserResponseSchema
from src.user.models import UserModel
from src.utils.db import get_db

auth_routes = APIRouter(prefix="/auth")


@auth_routes.post("/login", response_model=TokenSchema, status_code=status.HTTP_200_OK)
def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Session = Depends(get_db),
):
    return controller.login(form_data.username, form_data.password, db)


@auth_routes.get("/me", response_model=UserResponseSchema, status_code=status.HTTP_200_OK)
def read_current_user(current_user: UserModel = Depends(controller.get_current_user)):
    return current_user
