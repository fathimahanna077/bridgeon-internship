student={"name":"Hanna","age":20,"course":"Python"}
print("creating:",student)
print("access using[]:",student["name"])
print("access using .get():",student.get("course"))
student["age"]=21
print("updating:",student)
del student["course"]
print("deleting (del):",student)
student.pop("age")
print("pop:",student)
print(".keys():",student.keys())
print(".values():",student.values())
print(".items():",student.items())


