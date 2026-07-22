from pydantic import BaseModel
from typing import Optional

class UserSchema(BaseModel):
    name: str
    username: str
    email: str
    password: str


class UserResponseSchema(BaseModel):
    name: str
    username: str
    email: str
    id:  int