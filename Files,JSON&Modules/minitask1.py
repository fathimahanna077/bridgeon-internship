import json

students=[
    {"id":1,"name":"Hanna","mark":95},
    {"id":2,"name":"Afham","mark":20},
    {"id":3,"name":"Safa","mark":60},
    {"id":4,"name":"Sana","mark":75},
    {"id":5,"name":"Dog","mark":10}
]

with open("student.txt","w")as f:
    json.dump(students,f,indent=2)
print("data saved successfully")