import json
with open("student.txt","r")as file:
    students=json.load(file)
for student in students:
    print(
        f"ID:{student['id']},"
        f"Name:{student['name']},"
        f"Mark:{student['mark']}"
        )