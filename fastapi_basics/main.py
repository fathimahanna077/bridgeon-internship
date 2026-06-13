from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello FastAPI"}



from fastapi import FastAPI, HTTPException

app = FastAPI()

students = {
    1: {"name": "Hanna", "age": 22},
    2: {"name": "John", "age": 23},
    3: {"name": "Sara", "age": 21}
}


@app.get("/")
def home():
    return {"message": "Student API"}


@app.get("/students")
def get_students():
    return students


@app.get("/students/{student_id}")
def get_student(student_id: int):

    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return students[student_id]


@app.get("/search")
def search(q: str = None, limit: int = 10):

    return {
        "query": q,
        "limit": limit
    }











from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

tasks = {}

class TaskCreate(BaseModel):
    title: str
    completed: bool = False

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    completed: Optional[bool] = None

class TaskResponse(BaseModel):
    id: int
    title: str
    completed: bool


@app.post(
    "/tasks",
    response_model=TaskResponse,
    status_code=201
)
def create_task(task: TaskCreate):

    task_id = len(tasks) + 1

    new_task = {
        "id": task_id,
        "title": task.title,
        "completed": task.completed
    }

    tasks[task_id] = new_task

    return new_task


@app.get(
    "/tasks/{task_id}",
    response_model=TaskResponse
)
def get_task(task_id: int):

    return tasks[task_id]






from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

tasks = {}


class Task(BaseModel):
    title: str
    completed: bool = False


@app.get("/")
def home():
    return {"message": "Task API Running"}


@app.get("/tasks")
def get_tasks():
    return list(tasks.values())


@app.get("/tasks/{task_id}")
def get_task(task_id: int):

    if task_id not in tasks:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return tasks[task_id]


@app.post("/tasks", status_code=201)
def create_task(task: Task):

    task_id = len(tasks) + 1

    new_task = {
        "id": task_id,
        "title": task.title,
        "completed": task.completed
    }

    tasks[task_id] = new_task

    return new_task


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):

    if task_id not in tasks:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    updated_task = {
        "id": task_id,
        "title": task.title,
        "completed": task.completed
    }

    tasks[task_id] = updated_task

    return updated_task


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):

    if task_id not in tasks:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    deleted_task = tasks.pop(task_id)

    return {
        "message": "Task deleted",
        "task": deleted_task
    }





from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="Task CRUD API")

tasks = {}
next_id = 1


class TaskCreate(BaseModel):
    title: str
    completed: bool = False


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    completed: Optional[bool] = None


class TaskResponse(BaseModel):
    id: int
    title: str
    completed: bool


@app.get("/")
def home():
    return {"message": "Task CRUD API Running"}


@app.get("/tasks", response_model=list[TaskResponse])
def get_tasks():
    return list(tasks.values())


@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks[task_id]


@app.post("/tasks", response_model=TaskResponse, status_code=201)
def create_task(task: TaskCreate):
    global next_id

    new_task = {
        "id": next_id,
        "title": task.title,
        "completed": task.completed
    }

    tasks[next_id] = new_task
    next_id += 1

    return new_task


@app.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task: TaskCreate):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")

    updated_task = {
        "id": task_id,
        "title": task.title,
        "completed": task.completed
    }

    tasks[task_id] = updated_task
    return updated_task


@app.patch("/tasks/{task_id}", response_model=TaskResponse)
def patch_task(task_id: int, task: TaskUpdate):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")

    current_task = tasks[task_id]

    if task.title is not None:
        current_task["title"] = task.title

    if task.completed is not None:
        current_task["completed"] = task.completed

    return current_task


@app.patch("/tasks/{task_id}/complete", response_model=TaskResponse)
def complete_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")

    tasks[task_id]["completed"] = True
    return tasks[task_id]


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")

    deleted_task = tasks.pop(task_id)

    return {
        "message": "Task deleted",
        "task": deleted_task
    }


















from fastapi import APIRouter

router = APIRouter()

tasks = {
    1: {"id": 1, "title": "Learn FastAPI"},
    2: {"id": 2, "title": "Build CRUD API"}
}


@router.get("/")
def get_tasks():
    return list(tasks.values())


@router.get("/{task_id}")
def get_task(task_id: int):
    return tasks.get(task_id, {"error": "Task not found"})


@router.post("/")
def create_task():
    new_task = {
        "id": len(tasks) + 1,
        "title": "New Task"
    }

    tasks[new_task["id"]] = new_task

    return new_task