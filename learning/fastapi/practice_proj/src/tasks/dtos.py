from typing import Optional
from pydantic import BaseModel

class  TaskSchema(BaseModel):
    title: str
    description: str
    is_completed: bool = False


class TaskUpdateSchema(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    is_completed: Optional[bool] = None


class TaskResponseSchema(BaseModel):
    id: int
    title: str
    # description: str
    # is_completed: bool