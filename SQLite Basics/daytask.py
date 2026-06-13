import sqlite3

DB_NAME = "students.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        marks REAL NOT NULL
    )
    """)

    conn.commit()
    conn.close()


def insert_student(name, marks):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students (name, marks) VALUES (?, ?)",
        (name, marks)
    )

    conn.commit()
    conn.close()


def get_all_students():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    conn.close()

    return students


def get_student_by_id(student_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE id = ?",
        (student_id,)
    )

    student = cursor.fetchone()

    conn.close()

    return student


def update_marks(student_id, new_marks):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE students SET marks = ? WHERE id = ?",
        (new_marks, student_id)
    )

    conn.commit()
    conn.close()


def delete_student(student_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM students WHERE id = ?",
        (student_id,)
    )

    conn.commit()
    conn.close()


def get_students_above(threshold):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE marks > ?",
        (threshold,)
    )

    students = cursor.fetchall()

    conn.close()

    return students


def menu():
    create_table()

    while True:
        print("\n1. Add Student")
        print("2. View All Students")
        print("3. Get Student By ID")
        print("4. Update Marks")
        print("5. Delete Student")
        print("6. Students Above Threshold")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter name: ")
            marks = float(input("Enter marks: "))
            insert_student(name, marks)

        elif choice == "2":
            for student in get_all_students():
                print(student)

        elif choice == "3":
            student_id = int(input("Enter student ID: "))
            print(get_student_by_id(student_id))

        elif choice == "4":
            student_id = int(input("Enter student ID: "))
            new_marks = float(input("Enter new marks: "))
            update_marks(student_id, new_marks)

        elif choice == "5":
            student_id = int(input("Enter student ID: "))
            delete_student(student_id)

        elif choice == "6":
            threshold = float(input("Enter threshold: "))
            for student in get_students_above(threshold):
                print(student)

        elif choice == "7":
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    menu()