from fastapi import HTTPException

from src.tasks.dtos import TaskSchema, TaskUpdateSchema, TaskResponseSchema
from sqlalchemy.orm import Session
from src.tasks.models import *
from src.user.models import UserModel


def create_task(body: TaskSchema, db: Session, user:UserModel):
    new_task = TaskModel(**body.model_dump(), user_id=user.id)
    db.add(new_task)

    try:
        db.commit()
    except Exception:
        db.rollback()
        raise

    db.refresh(new_task)
    return new_task

def fetch_all(db: Session, user: UserModel):
    tasks = db.query(TaskModel).filter(TaskModel.user_id == user.id).all()
    return tasks

def fetch_task(task_id: int, db: Session, user: UserModel):
    task = db.query(TaskModel).filter(TaskModel.id == task_id, TaskModel.user_id == user.id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

def update_task(task_id: int, body: TaskUpdateSchema, db: Session, user: UserModel):
    task = db.query(TaskModel).filter(TaskModel.id == task_id, TaskModel.user_id == user.id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    for field, value in body.model_dump(exclude_unset=True).items():
        setattr(task, field, value)

    db.commit()
    db.refresh(task)

    return task


def delete_task(task_id: int, db: Session, user: UserModel):
    task = db.query(TaskModel).filter(TaskModel.id == task_id, TaskModel.user_id == user.id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(task)
    db.commit()

    return None         # delete tasks doesnt return anything

