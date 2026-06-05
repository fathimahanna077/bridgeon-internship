def my_decorator(func):

    def wrapper(*args, **kwargs):
        print("Before")

        result = func(*args, **kwargs)

        print("After")

        return result

    return wrapper


@my_decorator
def add(a, b):
    return a + b


print(add(10, 20))



