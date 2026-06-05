import json
student={"name":"Hanna","age":19,"city":"moodal"}
with open("student.json","w")as f:
    json.dump(student,f)

import json
with open("student.json","r")as f:
    data=json.load(f)
    print(data)

import json
with open("student.json","w")as f:
    json.dump(student,f,indent=4)

