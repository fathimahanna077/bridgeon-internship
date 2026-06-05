try:
    num=int(input("Enter a number:"))
    print(num)
except:
    print("invalid input")
else:
    print("you enterd:",num)

try:
    num=int(input("Enter a number:"))
    print(num)
except:
    print("invalid input")
finally:
    print("program finished")

age=int(input("enter your age:"))
if age<18:
    raise ValueError("Age must be 18 or above")
print("Allowed")

class InvalidMarkError(Exception):
    pass
mark=int(input("Enter mark:"))
if mark>100:
    raise InvalidMarkError("Mark cannot be above 100")
print("valid mark")

