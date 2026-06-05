def average(*marks):
    if len(marks) == 0:
        return "No marks given"

    avg = sum(marks) / len(marks)
    return avg


print(average(45, 50, 60))
print(average(80, 90))
print(average())

def safe_divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")

    return a / b


try:
    print(safe_divide(10, 0))

except ZeroDivisionError as e:
    print(e)


def calculate_grade(name,*marks):
    if len(marks) == 0:
        return "No marks given"
    for mark in marks:
        if mark<0 or mark>100:
            raise InvalidMarkError(f"invalid mark{mark} for{name}")



class InvalidMarkError(Exception):
    pass


def calculate_grade(name, *marks):

    if len(marks) == 0:
        return name, "No Marks", "No Grade"

    for mark in marks:
        if mark < 0 or mark > 100:
            raise InvalidMarkError(
                f"Invalid mark {mark}"
            )

    average = sum(marks) / len(marks)

    if average >= 90:
        grade = "A"

    elif average >= 75:
        grade = "B"

    elif average >= 50:
        grade = "C"

    else:
        grade = "F"

    return name, round(average, 2), grade


def generate_report(students):

    print("-" * 40)
    print(f"{'Name':<10} {'Average':<10} {'Grade'}")
    print("-" * 40)

    for student in students:

        try:
            result = calculate_grade(*student)

            print(
                f"{result[0]:<10} "
                f"{result[1]:<10} "
                f"{result[2]}"
            )

        except InvalidMarkError as e:
            print(f"{student[0]:<10} ERROR: {e}")

    print("-" * 40)


students = [
    ("Ali", 95, 90, 85),
    ("Sara", 150, 80),
    ("John",),
    ("Maya", 40, 50, 60),
    ("Tom", -5, 70)
]

generate_report(students)











        

