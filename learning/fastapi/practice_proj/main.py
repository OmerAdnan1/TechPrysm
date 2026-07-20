from fastapi import FastAPI, Request
from src.utils.db import Base, engine
from src.tasks.router import task_routes
from src.user.router import user_routes
from src.auth.router import auth_routes

Base.metadata.create_all(engine)

app = FastAPI(title="This is a practice project for FastAPI", description="This is a practice project for FastAPI")
app.include_router(task_routes)
app.include_router(user_routes)
app.include_router(auth_routes)





