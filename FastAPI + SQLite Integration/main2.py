from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from database import (
    init_db,
    db_get_all_tasks,
    db_get_task,
    db_create_task,
    db_update_task,
    db_delete_task
)

app = FastAPI()


@app.on_event("startup")
def startup():
    init_db()


class Task(BaseModel):
    title: str
    description: str
    status: str


@app.get("/")
def home():
    return {"message": "Task API Running"}


@app.post("/tasks")
def create_task(task: Task):
    return db_create_task(task.model_dump())


@app.get("/tasks")
def get_tasks(status: str = None):
    return db_get_all_tasks(status)


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    task = db_get_task(task_id)

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return task


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):
    updated = db_update_task(
        task_id,
        task.model_dump()
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return updated


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    deleted = db_delete_task(task_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return {"message": "Task deleted"}