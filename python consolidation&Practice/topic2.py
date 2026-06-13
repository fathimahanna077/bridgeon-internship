




def my_decorator(func):

    def wrapper():
        print("before function")

        func()

        print("After function")

    return wrapper
@my_decorator
def greet():
    print("Hello")
greet()



def greet(name:str)->str:
    return f"Hello, {name}"
print(greet("Hanna"))


def add(a: int, b:int)->int:
    return a+b
print(add(10,20))

def average(a: float,b: float)->float:
    return (a+b)/2
print(average(10.5,20.5))



import json
topics=[
    {
        "id":1,
        "title":"Python"
    }
]
with open("topics.json","w")as file:
    json.dump(topics,file,indent=4)
    








        


