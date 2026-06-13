import sqlite3

DB_NAME = "tasks.db"


def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            status TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def db_get_all_tasks(status=None):
    conn = get_connection()

    if status:
        rows = conn.execute(
            "SELECT * FROM tasks WHERE status = ?",
            (status,)
        ).fetchall()
    else:
        rows = conn.execute(
            "SELECT * FROM tasks"
        ).fetchall()

    conn.close()

    return [dict(row) for row in rows]


def db_get_task(task_id):
    conn = get_connection()

    row = conn.execute(
        "SELECT * FROM tasks WHERE id = ?",
        (task_id,)
    ).fetchone()

    conn.close()

    return dict(row) if row else None


def db_create_task(data):
    conn = get_connection()

    cursor = conn.execute(
        """
        INSERT INTO tasks (title, description, status)
        VALUES (?, ?, ?)
        """,
        (
            data["title"],
            data["description"],
            data["status"]
        )
    )

    conn.commit()

    task_id = cursor.lastrowid

    row = conn.execute(
        "SELECT * FROM tasks WHERE id = ?",
        (task_id,)
    ).fetchone()

    conn.close()

    return dict(row)


def db_update_task(task_id, data):
    conn = get_connection()

    conn.execute(
        """
        UPDATE tasks
        SET title = ?, description = ?, status = ?
        WHERE id = ?
        """,
        (
            data["title"],
            data["description"],
            data["status"],
            task_id
        )
    )

    conn.commit()

    row = conn.execute(
        "SELECT * FROM tasks WHERE id = ?",
        (task_id,)
    ).fetchone()

    conn.close()

    return dict(row) if row else None


def db_delete_task(task_id):
    conn = get_connection()

    cursor = conn.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,)
    )

    conn.commit()

    deleted = cursor.rowcount > 0

    conn.close()

    return deleted