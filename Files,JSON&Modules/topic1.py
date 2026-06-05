
with open("student.txt","r")as f:
 data=f.read()
 print(data)
 f.close()
with open("student.txt","w")as f:
 f.write("I love afham\n")
 f.write("by Hanna")
 f.close()
with open("student.txt","a")as f:
 f.write("\nWelcome")
with open("student.txt","r")as f:
 lines=f.readlines()
print(lines)