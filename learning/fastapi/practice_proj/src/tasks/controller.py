from fastapi import HTTPException

from src.tasks.dtos import TaskSchema, TaskUpdateSchema, TaskResponseSchema
from sqlalchemy.orm import Session
from src.tasks.models import *

def create_task(body: TaskSchema, db: Session):
    new_task = TaskModel(**body.model_dump())
    db.add(new_task)

    try:
        db.commit()
    except Exception:
        db.rollback()
        raise

    db.refresh(new_task)
    return new_task

def fetch_all(db: Session):
    tasks = db.query(TaskModel).all()
    return tasks

def fetch_task(task_id: int, db: Session):
    task = db.query(TaskModel).get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

def update_task(task_id: int, body: TaskUpdateSchema, db: Session):
    task = db.get(TaskModel, task_id)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    for field, value in body.model_dump(exclude_unset=True).items():
        setattr(task, field, value)

    db.commit()
    db.refresh(task)

    return task


def delete_task(task_id: int, db: Session):
    task = db.query(TaskModel).get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(task)
    db.commit()

    return None         # delete tasks doesnt return anything

