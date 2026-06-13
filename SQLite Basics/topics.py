import sqlite3
conn = sqlite3.connect("tasks.db")

import sqlite3

conn=sqlite3.connect("task.db")
cursor=conn.cursor()

cursor.execute(
    "INSERT INTO tasks (title, completed)VALUES (?,?)"
    ("Learn FastAPI", False)
)

conn.commit()
conn.close()
