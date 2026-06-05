def greet(name):
    return f"Hello, {name}!"


def calculate_grade(marks):
    average = sum(marks) / len(marks)

    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 50:
        return "C"
    else:
        return "F"