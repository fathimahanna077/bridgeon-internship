print("CLASS KEYWORD:")
class student:
    pass

print("KEYWORD:")
class student:
    pass
s1=student()
s2=student()
print(s1)
print(s2)

class student:
 def __init__(self,name):
    self.name=name
s1=student("Anu")
print(s1.name)

class student:
   def __init__(self):
      print("student object created")
s1=student()


class student:
   def __init__(self, name):
      self.name=name
s1=student("Anu")
print(s1.name)

class student:
   def student(self, name, mark):
      self.name=name
      self.mark=mark
s1=student("Anu",95)
print(s1.name)
print(s2.name)


class Student:

    school = "ABC School"

    def __init__(self, name):
        self.name = name

s1 = Student("Anu")
s2 = Student("Rahul")

print(s1.school)
print(s2.school)

