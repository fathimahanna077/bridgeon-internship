# ==========================
# 1. Create a Dictionary
# ==========================

student = {
    "name": "Hanna",
    "age": 21,
    "course": "Python"
}

print("Original Dictionary:")
print(student)

# ==========================
# 2. Access Values
# ==========================

print("\nAccess with []:")
print(student["name"])

print("\nAccess with get():")
print(student.get("age"))

# get() returns None if key doesn't exist
print(student.get("email"))

# ==========================
# 3. Update Values
# ==========================

student["age"] = 22
student["city"] = "Calicut"

print("\nAfter Update:")
print(student)

# ==========================
# 4. Delete Items
# ==========================

del student["city"]

print("\nAfter del:")
print(student)

removed = student.pop("course")

print("\nRemoved Value:")
print(removed)

print(student)

# ==========================
# 5. keys()
# ==========================

print("\nKeys:")
print(student.keys())

# ==========================
# 6. values()
# ==========================

print("\nValues:")
print(student.values())

# ==========================
# 7. items()
# ==========================

print("\nItems:")
print(student.items())

# ==========================
# 8. Loop Through Dictionary
# ==========================

print("\nLoop Through Keys:")

for key in student:
    print(key)

print("\nLoop Through Values:")

for value in student.values():
    print(value)

print("\nLoop Through Key-Value Pairs:")

for key, value in student.items():
    print(key, ":", value)

# ==========================
# 9. Nested Dictionary
# ==========================

students = {
    "student1": {
        "name": "Anu",
        "age": 20
    },
    "student2": {
        "name": "Rahul",
        "age": 22
    }
}

print("\nNested Dictionary:")
print(students)

print("\nAccess Nested Values:")
print(students["student1"]["name"])
print(students["student2"]["age"])

# ==========================
# 10. Dictionary Comprehension
# ==========================

squares = {x: x * x for x in range(1, 6)}

print("\nDictionary Comprehension:")
print(squares)

# ==========================
# 11. Check if Key Exists
# ==========================

print("\nKey Exists:")
print("name" in student)
print("email" in student)

# ==========================
# 12. Length of Dictionary
# ==========================

print("\nLength:")
print(len(student))