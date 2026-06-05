class Student:

    school = "ABC School"

    def __init__(self, name):
        self.name = name

s1 = Student("Anu")
s2 = Student("Rahul")

print(s1.school)
print(s2.school)

class student:
    def __init__(self,name):
        self.name=name
    def display(self):
        print("Name:",self.name)
s1=student("Anu")
s1.display()



class student:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return f"Student Name:{self.name}"
    s1=student("Anu")
    print(s1)

