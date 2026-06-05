def greet(word):
    print(word)
greet("hello")

def greet(function):
    print(function)
greet("Welcome to Python")

def student(name,age):
    print("Name:",name)
    print("Age:",age)
student(name="Ravi",age=19)

def numbers(a,b):
    print(a*b)
numbers(5,4)

def person(city,name):
    print(name, "lives in", city)
person(city="Calicut",name="Hanna")

def greet(name,message="Hello"):
    print(message,name)
greet("Ravi")

def power(number, exponent=2):
    print(exponent,number)
power(5)

def add_numbers(*args):
    print(args)
add_numbers(10,20,30)

def find_max(*args):
    print(max(args))
find_max(10,20,30,80)

def details(**kwargs):
    print(kwargs)
details(name="Hanna",age=19)



