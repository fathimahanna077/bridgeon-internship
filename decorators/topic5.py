def my_decorator(func):
    def wrapper():
        print("after funtion")

        func()

        print("before function")
    return wrapper
def greet():
    print("Hello") 
decorated=my_decorator(greet)
decorated()


def greet():
    print("hello")
decoratod=my_decorator(greet)
decoratod()