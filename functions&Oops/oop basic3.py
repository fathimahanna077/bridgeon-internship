class Animal:
    def eat(self):
        print("Animal is eating")
class Dog(Animal):
    pass
d1=Dog()
d1.eat()

class BankAccount:
    def show(self):
     print("Bank Account")
class savingsAccount(BankAccount):
    pass
s1=savingsAccount()
s1.show()

class BankAccount:
    def show(self):
        print("Bank Account")
        class SavingsAccount(BankAccount):
            pass
        s1 = SavingsAccount()
        s1.show()




class Person:
    def __init__(self, name):
        self.name = name
        class Student(Person):
            def __init__(self, name):
                super().__init__(name)
                s1 = Student("Anu")
                print(s1.name)


class Person:
    def __init__(self, name):
        self.name = name
class Student(Person):
    def __init__(self, name, mark):
        super().__init__(name)
        self.mark = mark
s1 = Student("Anu", 95)
print(s1.name)
print(s1.mark)



class Animal:
    def sound(self):
        print("Animal makes sound")
        class Dog(Animal):
            def sound(self):
                print("Dog barks")
                d1 = Dog()
                d1.sound()





class Animal:
    def sound(self):
        print("Animal Sound")
class Dog(Animal):
    def sound(self):
        super().sound()
        print("Dog Bark")
d1 = Dog()
d1.sound()
