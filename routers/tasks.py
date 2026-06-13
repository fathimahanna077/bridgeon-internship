from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from database import get_connection

from schemas import (
    TaskCreate,
    TaskUpdate
)

from routers.auth_routes import (
    get_current_user
)

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.get("/")
def get_tasks(
    current_user=Depends(
        get_current_user
    )
):

    with get_connection() as conn:

        rows = conn.execute(
            """
            SELECT * FROM tasks
            WHERE owner_email=?
            """,
            (current_user,)
        ).fetchall()

    return [dict(row) for row in rows]


@router.post("/")
def create_task(
    task: TaskCreate,
    current_user=Depends(
        get_current_user
    )
):

    with get_connection() as conn:

        conn.execute(
            """
            INSERT INTO tasks
            (title,description,owner_email)
            VALUES(?,?,?)
            """,
            (
                task.title,
                task.description,
                current_user
            )
        )

        conn.commit()

    return {"message": "Task created"}