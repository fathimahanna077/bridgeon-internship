import json
with open("student.txt","r")as f:
    data=json.load(f)
print(data)    