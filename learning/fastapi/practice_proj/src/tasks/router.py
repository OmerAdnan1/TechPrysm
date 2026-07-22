from fastapi import APIRouter, Depends, status
from src.tasks import controller
from src.tasks.dtos import TaskSchema, TaskUpdateSchema, TaskResponseSchema
from src.utils.db import get_db
from typing import List
from src.user.models import *
from src.auth.controller import get_current_user

task_routes = APIRouter(prefix="/tasks")

@task_routes.post("/create", response_model=TaskResponseSchema, status_code=status.HTTP_201_CREATED)
def create_task(body:TaskSchema, db = Depends(get_db), user:UserModel=Depends(get_current_user)):
    return controller.create_task(body, db, user)

@task_routes.get("/{task_id}", response_model=TaskResponseSchema, status_code=status.HTTP_200_OK)
def get_task(task_id: int, db = Depends(get_db), user:UserModel=Depends(get_current_user)):
    return controller.fetch_task(task_id, db, user)

@task_routes.get("/", response_model=List[TaskResponseSchema], status_code=status.HTTP_200_OK)
def get_task(db = Depends(get_db), user:UserModel=Depends(get_current_user)):
    return controller.fetch_all(db, user)


@task_routes.put("/update_task/{task_id}", response_model=TaskResponseSchema, status_code=status.HTTP_201_CREATED)
def update_task(task_id: int, body:TaskUpdateSchema, db = Depends(get_db), user:UserModel=Depends(get_current_user)):
    return controller.update_task(task_id, body, db, user)

@task_routes.delete("/delete_task/{task_id}", response_model=None, status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db = Depends(get_db), user:UserModel=Depends(get_current_user)):
    return controller.delete_task(task_id, db, user)
