import sqlite3
conn=sqlite3.connect("tasks.db")
cursor=conn.cursor()
cursor.execute("""
               CREATE TABLE IF NOT EXISTS tasks(
               id INTEGER PRIMARY KEY,
               title TEXT NOT NULL,
               completed BOOLEAN NOT NULL
)
               """)
cursor.execute(
    "INSERT INTO tasks(title,completed)VALUES(?,?)",
("Learn SQLite",False)
)
conn.commit()
cursor.execute("SELECT * FROM tasks")

for row in cursor.fetchall():
    print(row)
conn.close()