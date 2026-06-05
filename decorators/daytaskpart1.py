from datetime import datetime


def log_call(func):

    def wrapper(*args, **kwargs):

        with open("log.txt", "a") as file:
            file.write(
                f"{datetime.now()} | "
                f"{func.__name__} | "
                f"args={args} | kwargs={kwargs}\n"
            )

        return func(*args, **kwargs)

    return wrapper


@log_call
def add(a, b):
    return a + b


@log_call
def greet(name):
    return f"Hello {name}"


@log_call
def multiply(a, b):
    return a * b


print(add(10, 20))
print(add(5, 7))

print(greet("Afham"))
print(greet("John"))

print(multiply(2, 3))